from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from first_app.models import UserProfile, Post
from django.contrib.auth.models import User


# Create your views here.

def index(request):
	return render(request, 'index.html')

def profile(request, user_id):
	user = User.objects.get(id=user_id)
	posts = Post.objects.all()
	return render(request, 'profile.html', {'user': user, 'posts': posts})