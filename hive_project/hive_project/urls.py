from django.contrib import admin
from django.urls import path, include
from first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_app/', include('first_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile_app/', include('profile_app.urls')),


]
