from django.urls import include, path
from . import views
from . import forms
from django.conf.urls import url, include

app_name = 'first_app'

urlpatterns = [
	path('', views.index, name='index'),
	path('signup', views.signup, name='signup'),
	path('post/new', views.post_new, name='post_new'),
	path('post/edit/', views.post_edit, name='post_edit'),
	path('logged_out/', views.logged_out, name='logged_out'),
	path('follow/<int:user_id>/', views.follow, name='follow'),
	path('unfollow/<int:user_id>', views.unfollow, name='unfollow'),
	path('all_profiles/', views.all_profiles, name='all_profiles'),

]
# first_app/follow/<int:user_profile_id>


