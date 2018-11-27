from django.urls import include, path
from . import views
from . import forms

app_name = 'first_app'

urlpatterns = [
	path('', views.index, name='index'),
	path('profile/<int:user_id>/', views.profile, name='profile'),
	path('signup', views.signup, name='signup'),
]


