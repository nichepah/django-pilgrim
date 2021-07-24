from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.template import loader


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


# latest definition works; here index is defined again
def index(request):
	latest_question_list = Question.objects.order_by('pub_date')[:5]
	output = ', '.join([q.question_text for q in latest_question_list])
	return HttpResponse(output)


# latest definition works; here index is defined again
# this works with template
def index(request):
	latest_question_list = Question.objects.order_by('pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	return HttpResponse(template.render(context, request))


