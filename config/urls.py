from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home_page(request):
    return render(request, 'base.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('feedback/', include('feedback.urls')),
    path('', home_page, name='houme')
]
