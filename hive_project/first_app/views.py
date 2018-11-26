from django.shortcuts import render
from first_app.models import UserProfile, Post
#from . import forms
import datetime

# Create your views here.

def index(request):
	posts = Post.objects.all().order_by('-date')[:30]
	return render(request, 'index.html', { 'posts': posts })

def signup(request):
	return render(request, 'signup.html') 

def login(request):
	return render(request, 'login.html')
