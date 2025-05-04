from django.urls import path
from .views import *

urlpatterns = [
        path('', feedback, name='feedback'),
        path('list', feedback_list, name = 'feedback list'),
        ]
