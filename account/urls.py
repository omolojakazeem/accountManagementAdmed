from .views import register, profile
from django.urls import path

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='homepage'),
]
