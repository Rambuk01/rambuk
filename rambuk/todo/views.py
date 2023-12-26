from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from .models import TodoItem
from .forms import TodoItemForm
# Create your views here.
def index(request):
    todos = TodoItem.objects.all().order_by('-created_at')
    form = TodoItemForm()
    return render(request, 'todo/index.html', {'form': form, 'todos': todos})
    #return HttpResponse("Hello there!", {'request': request})

def create_todo(request):
    form = TodoItemForm()
    todos = TodoItem.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            todos = TodoItem.objects.all().order_by('-created_at')
            return HttpResponseRedirect(request.path_info)
    return render(request, 'todo/index.html', {'todos': todos, 'form': form})
    
def delete_todo(request, todo_id):
    todo = TodoItem.objects.get(pk=todo_id)
    todo.delete()

    form = TodoItemForm()
    todos = TodoItem.objects.all().order_by('-created_at')
    return HttpResponseRedirect(reverse('todo:index'))