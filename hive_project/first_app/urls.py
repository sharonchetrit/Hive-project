from django.urls import path, include
from . import views

app_name = 'first_app'

urlpatterns = [
	path('', views.index, name='index'),
	path('profile/<int:user_id>/', views.profile, name='profile')
]



