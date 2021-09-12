from django.conf.urls import url
from django.middleware.csrf import get_token
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
import time

# Create your views here.
from django.urls import reverse

def parse(request):
    """
    This function parses the information from the react form into our computation script using a GET request.
    """
    context = {}
    return render(request, 'results.html', context)
