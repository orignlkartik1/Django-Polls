from django.shortcuts import render
from django.http import HttpResponse as ht

def index(request):
    return ht("Hello World")
# Create your views here.
