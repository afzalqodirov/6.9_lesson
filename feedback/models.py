from django.db import models
from django.utils import timezone

# Create your models here.
class Feedback(models.Model):
    student_name = models.CharField(max_length = 150, default = 'anonymus' )
    message = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.feedback

    class Meta:
        db_table = 'feedback'
