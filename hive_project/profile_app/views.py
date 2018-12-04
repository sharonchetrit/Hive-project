from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from first_app.models import UserProfileInfo, Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from . import forms
import datetime
from django.utils import timezone



@login_required
def view_profile(request):
	user_id = request.user.id
	user = User.objects.get(id=user_id)
	profile = UserProfileInfo.objects.get(user=user)
	posts = Post.objects.filter(user=profile)

	return render(request, 'profile.html', {'profile': profile, 'posts': posts})

@login_required
def edit_profile(request):
	if request.method == 'POST':
		user_form = forms.EditProfileForm(request.POST, instance=request.user)
		profile_form = forms.UserProfileInfoForm(request.POST, instance=request.user)
		User.objects.filter(id=request.user.id).update(
			first_name='first_name',
			last_name='last_name',
			)
		UserProfileInfo.objects.filter(id=request.user.id).update(
			bio='bio')


		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return redirect(reverse('profile_app:view_profile'))


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

def users_profiles(request, user_id):
	user = User.objects.get(id=user_id)
	profile = UserProfileInfo.objects.get(user=user)
	posts = Post.objects.filter(user=profile)

	return render (request, 'profile/users_profiles.html', {'user':user, 'profile':profile, 'posts':posts})
	








