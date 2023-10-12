from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Task
# Create your views here.

def taskList(request):
    return HttpResponse('To Do List')

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/all_tasks.html'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    template_name = 'base/delete_task.html'


