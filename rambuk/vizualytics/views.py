from django.shortcuts import render
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.http import Http404, JsonResponse
from django.urls import reverse
#from .models import Question, Choice
from django.views import generic

# functions
from .functions.jobbean_functions import get_jobs_municipality

def view_request(request):
    req_str = request.GET.get('param')
    city_jobs_dict, total_jobs = get_jobs_municipality(req_str)
    return JsonResponse(city_jobs_dict)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class IndexView(generic.TemplateView):
    template_name = "vizualytics/index.html"

    #context_object_name = "latest_question_list"

