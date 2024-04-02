from django.shortcuts import render

from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
#from .models import Question, Choice
from django.views import generic
"""
# Create your views here.
class IndexView():
    template_name = "vizualytics/index.html"
    context_object_name = "latest_question_list"
"""
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class IndexView(generic.TemplateView):
    template_name = "vizualytics/index.html"
    #context_object_name = "latest_question_list"