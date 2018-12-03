from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from first_app.models import UserProfileInfo, Post
from django.contrib.auth.models import User
from django.urls import reverse


# Create your views here.

def index(request):
	posts = Post.objects.all()
	return render(request, 'index.html', { 'posts': posts })

def login(request):
	return render(request, 'login.html')

def profile(request, user_id):
	user = User.objects.get(id=user_id)
	posts = Post.objects.all()
	return render(request, 'profile.html', {'user': user, 'posts': posts})

def signup(request):
	registered = False

	if request.method == 'POST':
		user_form = forms.UserForm(data=request.POST)
		profile_form = forms.UserProfileInfoForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.set_password)
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


def logged_out(request):
	return render (request, 'registration/logout.html')

def following(request):
	user_profile = UserProfileInfo.objects.get(id=request.user.id)
	following = user_profile.following.all()
	profiles = UserProfileInfo.objects.all()
	for profile in profiles:
		if profile.user in following:
			profile.is_followed_by_me = True
	return render(request, 'users_profiles.html', {
		'profiles': profiles,
		'following': following
	})

def follow (request):
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


