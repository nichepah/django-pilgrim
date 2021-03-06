from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

from django.contrib import admin

# Create your models here.


class Question(models.Model):
	question_text = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')


	def __str__(self):
		return self.question_text


	def was_published_recently(self):
		''' 
		A custom method to check if question is recent
		'''
		now = timezone.now()
		return now - timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	choice_text = models.CharField(max_length=10)
	votes = models.IntegerField(default=0)


	def __str__(self):
		return self.choice_text



