from django.shortcuts import render
from .models import task
# Create your views here.

def task_list(request):
    tasks = task.objects.order_by('datedeadline')
    return render(request, 'task/task_list.html', {'tasks': tasks})
