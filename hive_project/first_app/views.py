from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from first_app.models import UserProfileInfo, Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.utils import timezone


# from django.forms import formset_factory, BaseFormSet

def index(request):
	posts = Post.objects.all().order_by('-date')[:30]
	return render(request, 'index.html', { 'posts': posts })

def login(request):
	return render(request, 'login.html')

@login_required
def all_profiles(request):
	users = User.objects.all()
	return render(request, 'profile/all_profiles.html', {'users': users})

@login_required
def following(request, user_id):
	user_logged_in= request.user
	user_followed= User.objects.get(id=user_id)
	profile1=UserProfileInfo.objects.get(user=user_logged_in)
	profile1.following.add(user_followed)
	profile1.save()

	return  redirect(reverse('profile_app:all_profiles'))




@login_required
def view_profile(request):
	# args = {'user':request.user}
	user = User.objects.get(id=request.user.id)
	profile = UserProfileInfo.objects.get(user=user)

	return render(request, 'profile/profile.html', {'profile': profile})

def signup(request):
	registered = False

	if request.method == 'POST':
		user_form = forms.UserForm(data=request.POST)
		profile_form = forms.UserProfileInfoForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			raw_password = user_form.cleaned_data.get('password')
			user.set_password(raw_password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']

			profile.save()
			registered = True

			return redirect(reverse('first_app:index'))

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = forms.UserForm()
		profile_form = forms.UserProfileInfoForm()

	return render(request, 'signup.html', {
								'user_form': user_form,
								'profile_form': profile_form,
								'registered': registered
								})



def logged_out(request):
	return render (request, 'registration/logout.html')




@login_required
def edit_profile(request):
	# if request.user.is_authenticated() and request.user.id == user.id:
	if request.method == 'POST':
		user_form = forms.EditProfileForm(request.POST, instance=request.user)
		profile_form = forms.UserProfileInfoForm(request.POST, instance=request.user)
		User.objects.filter(id=request.user.id).update(
			first_name='first_name',
			last_name='last_name',
			)


		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return redirect('profile_app:view_profile')

		else:
			return HttpResponse('Please correct the error bellow')

	else:
		# profile = UserProfileInfo.objects.get(id=user_id)
		user_form = forms.EditProfileForm(instance=request.user)
		profile_form = forms.UserProfileInfoForm(instance=request.user)
	
	return render(request, 'profile/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})




@login_required
def change_password(request):
	if request.method == 'POST':
		form = forms.PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			return redirect(reverse('profile_app:view_profile'))
		else:
			return redirect(reverse('profile_app:change_password'))

	else:
		form = PasswordChangeForm(user=request.user)
		return render(request, 'profile/change_password.html', {'form': form})


@login_required
def account_edit(request):
	profile_form = forms.EditProfileForm()
	password_form = forms.PasswordChangeForm()

	

	return render(request, 'profile/account_edit.html', {
		'profile_form': profile_form, 
		'password_form': password_form
		})


def post_new(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return redirect('first_app:post_detail', pk=post.pk)

    else:
        form = forms.PostForm()
    return render(request, 'post_edit.html', {'form': form})


def post_edit(request):
    post = forms.PostForm(request.POST)
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('first_app:post_detail')
    else:
        form = forms.PostForm(request.post)
    return render(request, 'post_edit.html', {'form': form})




def post_list(request):
    pass


def post_detail(request):
    pass






# add user_profile_id insede bracket

	
	# get user from request 

 #    if request.method == 'POST':
 #    	if request.user.is_authenticated():
 #        	user_logged_in_id = request.user.id

 #        	if user_form.is_valid() and profile_form.is_valid():
	# # get user profile from user - 1
	# # get U.P to follow from parameter -2
	# # add following 1 on 2
	# pass




# def signup(request):
#   if request.method == 'POST':
#       form = forms.SignUpForm(request.POST)
#       if form.is_valid():
#           form.save()
#           username = form.cleaned_data.get('username')
#           raw_password = form.cleaned_data.get('password1')
#           user = authenticate(username=username, password=raw_password)
#           login(request, user)
#           return HttpResponse('Congratulation ! you created an account !')
#   else:
#       form = forms.SignUpForm()

#   return render(request, 'signup.html', {'form': form})

# def user_login(request):
#   context = {}
#   if request.method == 'POST':
#       pass
#   else:
#       return render(request, "login.html", context)



