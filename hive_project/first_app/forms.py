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
		fields = ('username', 'email', 'password', 'first_name', 'last_name')

class UserProfileInfoForm(forms.ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ('bio', 'profile_pic')


class SignUpForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(widget=forms.PasswordInput())

	def clean( self):
		all_clean_data = super().clean()
		return all_clean_data

class EditProfileForm(UserForm):
	password = None
	class Meta():
		model = User
		fields = ('email',
				  'username',
				  'first_name',
				  'last_name'
			)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('text',)
		widgets = {
			'text': forms.TextInput(attrs={
				'id': 'post-text', 
				'required': True,
				'placeholder': 'text',
				}),
		}


	# def clean(self):
	# 	all_clean_data = super().clean()
		# email = all_clean_data['email']
		# email_check = all_clean_data['email_check']

		# if email != email_check:
		# 	raise forms.ValidationError('Please, make sure emails match')
	


	# 	if User.objects.filter(email=email).exists():
	# 		raise ValidationError("Email already exists")
	# 	return email


# 	def clean(self):
	
# 		first_name = self.cleaned_data['first_name']
# 		last_name = all_clean_data['last_name']
# 		username = all_clean_data['username']
# 		email = all_clean_data['email']
		# verify_email = all_clean_data['verify_email']

		# if email != verify_email:
		#     raise forms.ValidationError('Make sure emails match')

