from django.shortcuts import render
from django.http import HttpResponse as ht, Http404
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-put_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
# Create your views here.
