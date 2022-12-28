from django.shortcuts import render

task = ["foo", "baz", "lol"]
# Create your views here.

def index(request):
  return render(request, "tasks/index.html", {
    "tasks": task
  })
