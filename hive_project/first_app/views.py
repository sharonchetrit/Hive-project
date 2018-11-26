from django.shortcuts import render
from first_app.models import UserProfile, Post
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from . import forms
from first_app.models import UserProfile, Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
	posts = Post.objects.all().order_by('-date')[:30]
	return render(request, 'index.html', { 'posts': posts })

def login(request):
	return render(request, 'login.html')

def profile(request, user_id):
	user = User.objects.get(id=user_id)
	posts = Post.objects.all()
	return render(request, 'profile.html', {'user': user, 'posts': posts})

def signup(request):
	if request.method == 'POST':
		form = forms.SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return HttpResponse('Congratulation ! you created an account !')
	else:
		form = forms.SignUpForm()

	return render(request, 'signup.html', {'form': form})

def user_login(request):
	context = {}
	if request.method == 'POST':
		pass
	else:
		return render(request, "login.html", context)


