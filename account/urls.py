from .views import register, profile,logout_user, login_user
from django.urls import path

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='user_profile'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
]
