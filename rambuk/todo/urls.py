from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('create-todo/', views.create_todo, name='create-todo'),
]