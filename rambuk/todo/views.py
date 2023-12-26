from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import TodoItem
from .forms import TodoItemForm
# Create your views here.
def index(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

    #return HttpResponse("Hello there!", {'request': request})

def create_todo(request):
    
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            todos = TodoItem.objects.all()
            return render(request, 'todo/index.html', {'todos': todos})
    else:
        form = TodoItemForm()
    return render(request, 'todo/create-todo.html', {'form': form})