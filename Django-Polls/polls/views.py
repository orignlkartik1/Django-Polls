from django.shortcuts import render
from django.http import HttpResponse as ht

def index(request):
    return ht("Hello World")
# Create your views here.

def detail(request,question_id):
    return ht("You are looking at the question %s" % question_id)

def results(request,question_id):
    return ht("You are looking at the results %s" %question_id)

def vote(request,question_id):
    return ht("You are looking at the results %s" %question_id)