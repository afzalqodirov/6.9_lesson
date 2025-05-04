from django.urls import path
from .views import *

urlpatterns = [
    path('', students_list, name='students'),
    path('add', student_create, name='student add'),
        ]
