from django.urls import include, path
from . import views
from . import forms
from django.conf.urls import url, include

app_name = 'first_app'

urlpatterns = [
	path('', views.index, name='index'),
	path('signup', views.signup, name='signup'),
	path('profile/', views.view_profile, name='view_profile'),
	path('profile/edit/', views.edit_profile, name='edit_profile'),
	path('change/password', views.change_password, name='change_password'),
	path('account/edit', views.account_edit, name='acccount_edit'),
	path('post/new', views.post_new, name='post_new'),
	path('post/detail', views.post_detail, name='post_detail'),
	path('post/list', views.post_list, name='post_list'),
	path('post/edit/', views.post_edit, name='post_edit'),
	path('logged_out/', views.logged_out, name='logged_out'),
]
# first_app/follow/<int:user_profile_id>


