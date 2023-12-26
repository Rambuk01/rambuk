from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import TodoItem
# Create your views here.
def index(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

    #return HttpResponse("Hello there!", {'request': request})