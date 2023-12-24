from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Question
# Create your views here.
def index(request):
    lastest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': lastest_question_list}
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse(f'Youre looking at question {question_id}')

def result(request, question_id):
    return HttpResponse(f'Youre looking at the result of question {question_id}')

def vote(request, question_id):
    return HttpResponse(f'Youre voting on question {question_id}')