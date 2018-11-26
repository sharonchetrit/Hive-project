from django import forms
from first_app.models import UserProfile, Post
from django.contrib.auth.models import User



class UserProfileForm(forms.ModelForm):
	class Meta():
		model = User
		fields = '__all__'

class AddUser(forms.ModelForm):
	class Meta():
		model = UserProfile
		fields = '__all__'

class AddTweet(forms.ModelForm):
	class Meta():
		model = Post
		fields = '__all__'