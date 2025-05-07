from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = EmailField()
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
