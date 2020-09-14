from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:slug>/', views.CategoryQuestionView.as_view(), name='category-polls'),
    path('<str:slug>/<int:pk>/', views.DetailView.as_view(), name='question-detail'),
    path('<str:slug>/<int:pk>/results/', views.ResultsView.as_view(), name='question-results'),
    path('<str:slug>/<int:pk>/vote/', views.question_vote, name='vote'),
]