from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. Youre at the polls index now.")

def detail(request, question_id):
    return HttpResponse(f'Youre looking at question {question_id}')

def result(request, question_id):
    return HttpResponse(f'Youre looking at the result of question {question_id}')

def vote(request, question_id):
    return HttpResponse(f'Youre voting on question {question_id}')