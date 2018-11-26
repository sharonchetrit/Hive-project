from django import forms
from first_app.models import UserProfile, Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




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

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email adress.')
	# confirm_password =forms.CharField(max_length=50, widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username', 
				  'first_name', 
				  'last_name', 
				  'email', 
				  'password1', 
				  'password2')

	def clean(self):
		cleaned_data = super(SignUpForm, self).clean()
		password = cleaned_data.get("password1")
		confirm_password = cleaned_data.get("password2")

		if password != confirm_password:
			raise forms.ValidationError(
				"password and confirm_password does not match"
			)

	def save(self, commit=True):
		user = super(SignUpForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
