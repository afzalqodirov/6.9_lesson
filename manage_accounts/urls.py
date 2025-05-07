from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name = 'register'),
    path('login/', sign_in, name = 'Login'),
    path('logout/', sign_out, name = 'Logout'),
    path('password-change', pass_change, name = 'pass change'),
        ]
