from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm

from django.contrib.auth.decorators import login_required


def home(request):
	boards = Board.objects.all()
	return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
	board = get_object_or_404(Board, pk=pk)
	return render(request, 'topics.html', {'board': board})


# Shows base.html
def base(request):
	return render(request, 'base.html')


@login_required
def new_topic(request, pk):
	board = get_object_or_404(Board, pk=pk)
	user = User.objects.first()
	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		if form.is_valid:
			topic = form.save(commit=False)
			topic.board = board
			topic.starter = user
			topic.save()
			post = Post.objects.create(
				message = form.cleaned_data.get('message'),
				topic = topic,
				created_by = user
				)
			return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
			
	else:
		form=NewTopicForm()
	return render(request, 'new_topic.html', {'board': board, 'form': form})