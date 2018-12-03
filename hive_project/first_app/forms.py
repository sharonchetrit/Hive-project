from django import forms
from first_app.models import UserProfileInfo, Post
from django.contrib.auth.models import User
from django.core import validators


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(), min_length=6)

	class Meta():
		model = User
		fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ('bio',)

	def clean_email(self):
		email = self.cleaned_data['email']
		username = self.cleaned_data['username']

# class FollowForm(ModelForm):

#     class Meta():
#         model = UserProfileInfo
#         fields = ('following')

#       def clean(self):
#       	#by doing this i check if the guy is in the list
#       	following = all_clean_data['following']

#       if User.objects.filter(username=self.cleaned_data['username']).exists():
      	

		
	# 	if User.objects.filter(email=email).exists():
	# 		raise ValidationError("Email already exists")
	# 	return email

# class SignUpForm(forms.ModelForm):
# 	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
# 	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
# 	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email adress.')
# 	botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

	
# 	class Meta():
# 		model = User
# 		fields = ('username', 
# 				  'first_name', 
# 				  'last_name', 
# 				  'email',
# 				  'password')

# 	def clean(self):
	
# 		first_name = self.cleaned_data['first_name']
# 		last_name = all_clean_data['last_name']
# 		username = all_clean_data['username']
# 		email = all_clean_data['email']
		# verify_email = all_clean_data['verify_email']

		# if email != verify_email:
		#     raise forms.ValidationError('Make sure emails match')

