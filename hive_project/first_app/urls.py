from django.urls import include, path
from . import views
from . import forms

app_name = 'first_app'

urlpatterns = [
	path('', views.index, name='index'),
	path('profile/<int:user_id>/', views.profile, name='profile'),
	path('signup', views.signup, name='signup'),
	path('profile/edit/', views.edit_profile, name='edit_profile'),
	url('change-password', views.edit_profile, name='edit_profile'),
]


