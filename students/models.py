from django.db import models

# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=200, unique=True)
    grade = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.full_name} in {self.grade}'

    class Meta:
        db_table = 'students'
