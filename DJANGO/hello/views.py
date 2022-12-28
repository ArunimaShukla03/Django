from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request, "hello/index.html")


def arunima(request):
  return HttpResponse("Hello Arunima!")

'''

def greet(request, name):
  return HttpResponse(f"Hello, {name.capitalize()}!")
  
'''

# A second way to write a greet function that does the same job while separating HTML is by the following way: 

def greet(request, name):
  return render(request,"hello/greet.html", {
    "name": name.capitalize()
  })