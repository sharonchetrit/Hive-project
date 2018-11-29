from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from first_app.models import UserProfileInfo, Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# from django.contrib.auth import UserChangeForm


# Create your views here.

def index(request):
<<<<<<< HEAD
    posts = Post.objects.all().order_by('-date')[:30]
    return render(request, 'index.html', { 'posts': posts })
=======
	posts = Post.objects.all()
	return render(request, 'index.html', { 'posts': posts })
>>>>>>> 2b648bae98c844fe2aaf375bd40c0f503dbb7cd3

# def user_login(request):
# 	context = {}
# 	if request.method == 'POST':
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		user = authenticate(request, username=username, password=password)
# 		if user:
# 			login(request, user)
# 			return HttpResponseRedirect(reverse('user_success'))
# 		else:
# 			context["error"] = "Provide valid credentials"
# 			return render(request, 'registration/login.html', context)
# 	else:
# 		return render(request, 'registration/login.html', context)

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

		  # if 'profile_pic' in request.FILES:
		  #   profile.profile_pic = request.FILES['profile_pic']
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


def view_profile(request):
	args = {'user':request.user}
	return render(request, 'profile.html', args)

	# user = User.objects.get(id=user_id)
	# posts = Post.objects.all()



@login_required
def edit_profile(request):
	if request.method == 'POST':
		form = forms.EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect(reverse('profile_app:edit_profile'))

	else:
		form = forms.EditProfileForm(instance=request.user)
	return render(request, 'profile/edit_profile.html', {'form': form})


@login_required
def change_password(request):
	if request.method == 'POST':
		form = forms.PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect(reverse('profile_app:view_profile'))
		else:
			return redirect(reverse('profile_app:change_password'))

	else:
		form = PasswordChangeForm(user=request.user)
		return render(request, 'profile/change_password.html', {'form': form})


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


