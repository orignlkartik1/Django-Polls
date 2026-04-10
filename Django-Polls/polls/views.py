from django.shortcuts import render
from django.http import HttpResponse as ht, Http404
from django.template import loader
from .models import Question


def index(request):
    atest_question_list = Question.objects.order_by("-put_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return ht(template.render(context, request))
# Create your views here.

def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

def results(request,question_id):
    return ht("You are looking at the results %s" %question_id)

def vote(request,question_id):
    return ht("You are looking at the results %s" %question_id)