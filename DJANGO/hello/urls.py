from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("arunima", views.arunima, name="arunima"),
  path("<str:name>", views.greet, name="greet")
]