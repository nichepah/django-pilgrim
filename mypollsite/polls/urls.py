from django.urls import path

from . import views

# add app_name to set application namespace

app_name = 'polls'
urlpatterns = [
path('', views.index, name='index'),
path('<int:question_id>', views.detail, name='detail'),
path('<int:question_id>/results/', views.results, name='results'),
path('<int:question_id>/vote/', views.vote, name='vote'),
]