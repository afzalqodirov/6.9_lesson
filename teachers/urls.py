from django.urls import path
from .views import *

urlpatterns = [
    path('', teachers_list, name='teachers'),
    path('add', teacher_form, name='teacher add'),
        ]
