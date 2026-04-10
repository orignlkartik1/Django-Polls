from django.shortcuts import render
from django.http import HttpResponse as ht

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-put_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return ht(output)
# Create your views here.

def detail(request,question_id):
    return ht("You are looking at the question %s" % question_id)

def results(request,question_id):
    return ht("You are looking at the results %s" %question_id)

def vote(request,question_id):
    return ht("You are looking at the results %s" %question_id)