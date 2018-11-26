from django.urls import include, path
from . import views

app_name = 'first_app'

urlpatterns = [
	path('', views.index, name='index'),
	path('signup.html', views.signup, name='signup'),
	path('login.html', views.login, name='login'), 
]



