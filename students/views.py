from django.shortcuts import render, redirect
from .models import Student 
from .forms import StudentForm

# Create your views here.

def students_list(request):
    return render(request, 'students_list.html', context={'students':Student.objects.all()})

def student_create(request):
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()

    return render(request, 'student_form.html', context={'form':form})
