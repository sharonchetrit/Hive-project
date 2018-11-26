<<<<<<< HEAD
from django.urls import include, path
=======
from django.urls import path, include
>>>>>>> signup
from . import views
from . import forms

app_name = 'first_app'

urlpatterns = [
<<<<<<< HEAD
	path('', views.index, name='index'),
	path('signup.html', views.signup, name='signup'),
	path('login.html', views.login, name='login'), 
=======
	path('', views.index, name=''),
	path('profile/<int:user_id>/', views.profile, name='profile'),
	path('signup', views.signup, name='signup'),
>>>>>>> signup
]



