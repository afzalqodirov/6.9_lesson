from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('houme')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form':form})

def sign_out(request):
    logout(request)
    return redirect('houme')

def sign_in(request):
    if request.method == "POST":
        user = authenticate(request, username = request.POST.get("username"), password = request.POST.get("password"))
        if user is not None:
            login(request, user)
            return redirect('houme')
    return render(request, 'login.html')

def pass_change(request):
    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new1_password = request.POST.get("new1_password")
        new2_password = request.POST.get("new2_password")
        if request.user.check_password(old_password) and old_password != new1_password and new1_password == new2_password:
            try:
                request.user.set_password(new1_password)
                request.user.save()
                return redirect('houme')
            except Exception as e:
                messages.error(request, e)
    return render(request, 'password_change.html')

