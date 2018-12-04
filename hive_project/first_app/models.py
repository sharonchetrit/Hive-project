from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User, unique=True, on_delete= models.CASCADE)
	bio = models.CharField(max_length=500)
	profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
	following = models.ManyToManyField(User, related_name='followers' ,symmetrical=False )

	def __repr__(self):
		return "<User {}>".format(self.user.username)

	def __str__(self):
		return self.user.username


class Post(models.Model):
	text = models.CharField(max_length=500)
	date = models.DateField()
	user = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE)

	def __repr__(self):
		return "<Post {}>".format(self.text)

	def __str__(self):
		return self.text


