<<<<<<< HEAD
from django.urls import include, path
=======
from django.urls import path, include
>>>>>>> signup
from . import views
from . import forms
from django.contrib.auth import views as auth_views

app_name = 'first_app'

urlpatterns = [
<<<<<<< HEAD
	path('', views.index, name='index'),
	path('profile/<int:user_id>/', views.profile, name='profile'),
	path('signup', views.signup, name='signup'),
	path('login', auth_views.LoginView.as_view(template_name='login.html')),
=======
<<<<<<< HEAD
	path('', views.index, name='index'),
	path('signup.html', views.signup, name='signup'),
	path('login.html', views.login, name='login'), 
=======
	path('', views.index, name=''),
	path('profile/<int:user_id>/', views.profile, name='profile'),
	path('signup', views.signup, name='signup'),
>>>>>>> signup
>>>>>>> master
]



