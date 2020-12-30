from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def home(request):

	return render(request,'main/home.html')


def compete(request):

	return render(request,'main/compete.html')	