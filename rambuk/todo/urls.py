from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('create-todo/', views.create_todo, name='create-todo'),
    path('delete-todo/<int:todo_id>', views.delete_todo, name='delete-todo')
]