from django.conf.urls import url
from django.middleware.csrf import get_token
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
import time

# Create your views here.
from django.urls import reverse
from ast import literal_eval
# from .src.pantry import main

def parse(request):
    """
    This function parses the information from the react form into our computation script using a GET request.
    """
    pantry = literal_eval(request.GET.get('pantries')[1:-1])
    items = literal_eval(request.GET.get('items')[1:-1])
    # shelves = literal_eval(request.GET.get('tasks')[1:-1])
    shelves = ""

    d = {"pantry": pantry, "items": items, "shelves": shelves}
    # for k in d:
    #     print(k, d[k], type(d[k]))
    ic = 1
    sc = 1
    if not 'dict' in str(type(items)):
        ic = len(items)
    if not 'dict' in str(type(shelves)):
        sc = len(shelves)

    context = d
    return render(request, 'parse.html', context)

def landing(request):
    """
    This function renders the landing tab
    """
    context = {}
    return render(request, 'landing_home.html', context)


def about(request):
    """
    This function renders the about tab
    """
    context = {}
    return render(request, 'landing_about.html', context)
