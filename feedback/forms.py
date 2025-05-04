from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        fields = ['student_name', 'message']
        model = Feedback
