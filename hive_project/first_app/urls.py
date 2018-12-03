from django.urls import include, path
from . import views
from . import forms
from django.conf.urls import url, include


app_name = 'first_app'

urlpatterns = [
	path('', views.index, name='index'),
	path('signup', views.signup, name='signup'),
	# path('profile/', views.view_profile, name='view_profile'),
	path('profile/', views.view_profile, name='view_profile'),
	path('profile/edit/', views.edit_profile, name='edit_profile'),
	path('change/password', views.change_password, name='change_password'),
	path('account/edit', views.account_edit, name='acccount_edit'),
]


