from django.urls import path

from . import views

app_name = 'vizualytics'
urlpatterns = [
    # added the word 'specifics'
    # path("specifics/<int:question_id>/", views.detail, name="detail"),
    #path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('ajax/', views.view_request, name='view_request'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]