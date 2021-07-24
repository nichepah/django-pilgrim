from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
	return HttpResponse("Hello, you are at the polls index.")


def detail(request, question_id):
	return HttpResponse("You are looking at qn %s." %question_id)


def results(request, question_id):
	response = "results of question %s."
	return HttpResponse(response %question_id)


def vote(request, question_id):
	return HttpResponse("You are voting on qn %s." %question_id)


