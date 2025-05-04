from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

# Create your views here.
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('houme')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', context={'form':form})

def feedback_list(request):
    return render(request, 'feedback_list.html', context={'feedbacks':Feedback.objects.all()})
