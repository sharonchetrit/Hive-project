from django.urls import include, path
from first_app import views
from django.conf.urls import url, include


app_name = 'profile_app'

urlpatterns = [
	# path('', views.index, name='index'),
	# path('profile/', views.view_profile, name='view_profile'),
	path('all_profiles/', views.all_profiles, name='all_profiles'),
	path('follow/<int:user_id>/', views.follow, name='follow'),
	path('unfollow/<int:user_id>', views.unfollow, name='unfollow'),
	path('profile/', views.view_profile, name='view_profile'),
	path('profile/edit/', views.edit_profile, name='edit_profile'),
	path('change/password', views.change_password, name='change_password'),
	path('account/edit', views.account_edit, name='acccount_edit'),

	

	# path('signup', views.signup, name='signup'),


]


