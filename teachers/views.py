from django.shortcuts import render, redirect
from .models import Teacher
from .forms import TeacherForm

# Create your views here.
def teachers_list(request):
    return render(request, 'teachers_list.html', context={'teachers':Teacher.objects.all()})

def teacher_form(request):
    if request.method=='POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    else:
        form = TeacherForm()
    return render(request, 'teacher_form.html', context={'form':form})
