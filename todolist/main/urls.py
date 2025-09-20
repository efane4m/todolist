from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
]