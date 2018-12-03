from django.urls import include, path
from . import views
from . import forms

app_name = 'first_app'

urlpatterns = [
	path('', views.index, name='index'),
	path('profile/<int:user_id>/', views.profile, name='profile'),
	path('signup', views.signup, name='signup'),
	path('logged_out/', views.logged_out, name='logged_out'),
	path('follow/<int:user_id>', views.follow, name='follow'),
	path('unfollow/<int:user_id>', views.unfollow, name='unfollow'),

	path('following', views.following, name='following'),
]
# first_app/follow/<int:user_profile_id>


