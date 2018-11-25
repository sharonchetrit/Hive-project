from django import forms
from first_app.models import UserProfile, Tweet


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile

class AddUser(forms.ModelForm):
	class Meta():
		model = UserProfile
		fields = '__all__'

class AddTweet(forms.ModelForm):
	class Meta():
		model = Tweet
		fields = '__all__'