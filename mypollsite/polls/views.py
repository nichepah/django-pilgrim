from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404


# Create your views here.


def index(request):
	return HttpResponse("Hello, you are at the polls index.")


# 2nd definition; here index is defined again
def index(request):
	latest_question_list = Question.objects.order_by('pub_date')[:5]
	output = ', '.join([q.question_text for q in latest_question_list])
	return HttpResponse(output)


# 3rd definition; here index is defined again
# this works with template
def index(request):
	latest_question_list = Question.objects.order_by('pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = { 'latest_question_list': latest_question_list }
	# return HttpResponse(template.render(context, request))
	# shortcut 
	return render(request, 'polls/index.html', context)


def detail(request, question_id):
	return HttpResponse("You are looking at qn %s." %question_id)


# 2nd definition for detail to raise 404 error
def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'polls/detail.html', {'question': question})


# 3rd definition for detail to raise 404 error
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
	response = "results of question %s."
	return HttpResponse(response %question_id)


def vote(request, question_id):
	return HttpResponse("You are voting on qn %s." %question_id)

