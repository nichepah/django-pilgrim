from django.urls import path

from . import views

# add app_name to set application namespace

app_name = 'polls'
urlpatterns = [
path('', views.IndexView.as_view(), name='index'),
path('<int:pk>/', views.DetailView.as_view(), name='detail'),
path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
path('<int:question_id>/vote/', views.vote, name='vote'),
]
