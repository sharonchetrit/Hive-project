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
import datetime
from django.utils import timezone



def index(request):
	posts = Post.objects.all().order_by('-date')[:30]
	print(posts)
	return render(request, 'index.html', { 'posts': posts })

def login(request):
	return render(request, 'login.html')


@login_required
def all_profiles(request):
	users = User.objects.all()
	userprofileinfo = UserProfileInfo.objects.get(user=request.user)
	following = userprofileinfo.following.all()
	return render(request, 'profile/all_profiles.html', {'users': users, 'following':following})

@login_required
def follow(request, user_id):
	user_logged_in = request.user
	user_followed = User.objects.get(id=user_id)
	profile_user_logged_in = UserProfileInfo.objects.get(user=user_logged_in)
	profile_user_logged_in.following.add(user_followed)
	profile_user_logged_in.save()

	return redirect(reverse('first_app:all_profiles'))

@login_required
def unfollow(request, user_id):
	user_logged_in = request.user
	user_followed = User.objects.get(id=user_id)
	profile_user_logged_in = UserProfileInfo.objects.get(user=user_logged_in)
	profile_user_logged_in.following.remove(user_followed)
	profile_user_logged_in.save()

	return redirect(reverse('first_app:all_profiles'))	

@login_required
def following(request):
	user_logged_in = request.user
	profile_user_logged_in = UserProfileInfo.objects.get(user=user_logged_in)
	following = profile_user_logged_in.following.all()

	return render(request, 'following.html', {'following': following})


@login_required
def followers(request):
	user_logged_in = request.user
	profile_user_logged_in = UserProfileInfo.objects.get(user=user_logged_in)
	followers = profile_user_logged_in.following.all()

	return render(request, 'followers.html', {'followers':followers})

@login_required
def view_profile(request):
	# args = {'user':request.user}
	user = User.objects.get(id=request.user.id)
	profile = UserProfileInfo.objects.get(user=user)
	posts = Post.objects.filter(profile=profile)

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

			return redirect(reverse('first_app:all_profiles'))

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
def post_new(request):
	user_id = request.user.id
	user = User.objects.get(id=user_id)
	profile = UserProfileInfo.objects.get(user=user)
	form = forms.PostForm()

	if request.method == 'POST':
		form = forms.PostForm(data=request.POST)

		if form.is_valid():
			text = form.cleaned_data['text']
			post = Post(text=text, profile=profile, date=datetime.datetime.now())
			post.save()

			return redirect('first_app:index')

	
	return render(request, 'post_new.html', {'form': form, 'user': user})

@login_required
def post_edit(request):
	# post = forms.PostForm(request.POST, instance=request.user)
	if request.method == 'POST':
		post_form = forms.PostForm(request.POST, instance=request.user)
		if post_form.is_valid():
			post = post_form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('first_app:post_edit')
		else:
			return HttpResponse('You cannot work')
	else:
		post_form = forms.PostForm(instance=request.user)
	return render(request, 'post_edit.html', {'post_form': post_form})







