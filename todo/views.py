from django.shortcuts import redirect, render
from . models import Task
from django.http import HttpResponse

# Create your views here.

def addTask(request):
    task = request.POST.get('task')
    Task.objects.create(task=task)
    return redirect('home')
