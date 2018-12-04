from django import forms
from first_app.models import UserProfileInfo, Post
from django.contrib.auth.models import User
from django.core import validators
# from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(), min_length=6)

	class Meta():
		model = User
		fields = ('username', 'email', 'password')


class EditProfileForm(UserForm):
	password = None
	class Meta():
		model = User
		fields = ('email',
				  'username',
				  'first_name',
				  'last_name'
			)

class UserProfileInfoForm(forms.ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ('bio', 'profile_pic')

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('text',)



