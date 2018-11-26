from django.contrib import admin
from first_app.models import UserProfile, Post

# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Post)