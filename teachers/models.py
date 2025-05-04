from django.db import models

# Create your models here.

choices = (('Math','math'), ('Physics','physics'), ('Science','science'), ('Art','art'))
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    experience_years = models.PositiveIntegerField()
    subject = models.CharField(max_length=200, choices=choices)
