from django import forms
from django.shortcuts import render

task = ["foo", "baz", "lol"]
# Create your views here.

class NewTaskForm(forms.Form):
  tasksss = forms.CharField(label="New Task:")
  priority = forms.IntegerField(label="Priority", min_value=1)

def index(request):
  return render(request, "tasks/index.html", {
    "tasks": task
  })
  
def add(request):
  if request.method == "POST":
    form = NewTaskForm(request.POST)

    if form.is_valid():
      tasksss = form.cleaned_data["tasksss"]
      task.append(tasksss)

    else:
      return render(request, "tasks/add.html", {
        "forms":form
      })

  return render(request, "tasks/add.html", {
    "forms":NewTaskForm
  })