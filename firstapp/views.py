from django.shortcuts import render
from .models import MyModel
from django.http import HttpResponse

# Create your views here.


def index(request):
    my_mod = MyModel(">><<")
    return HttpResponse("Hello World!")