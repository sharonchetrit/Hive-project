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
# from django.forms import formset_factory, BaseFormSet

def index(request):
    posts = Post.objects.all().order_by('-date')[:30]
    return render(request, 'index.html', { 'posts': posts })


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


def view_profile(request):
	args = {'user':request.user}
	return render(request, 'profile/profile.html', args)

	# user = User.objects.get(id=user_id)
	# posts = Post.objects.all()


@login_required
def edit_profile(request):
	if request.method == 'POST':
		form = forms.EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect(reverse('profile_app:view_profile'))

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


@login_required
def account_edit(request):
	profile_form = forms.EditProfileForm()
	password_form = forms.PasswordChangeForm()

	return render(request, 'profile/account_edit.html', {
		'profile_form': profile_form, 
		'password_form': password_form
		})


