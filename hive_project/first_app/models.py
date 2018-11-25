from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	bio = models.Charfield(max_length=500)
	profile_pic = models.ImageField(upload_to='', blank=True)
	# follows = models.ManyToManyField("self", related_name= 'followed_by')

	def __repr__(self):
		return "<User {}>".format(self.user.username)

	def __str__(self):
		return self.user_name

class Tweet(models.Model):
	text = models.Charfield(max_length=500)
	date = models.DateField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __repr__(self):
		return "<Tweet {}>".format(self.text)

	def __str__(self):
		return self.text
