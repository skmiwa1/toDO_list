from django.shortcuts import render
from django.views import generic

from list.models import Task


# Create your views here.
class TaskListView(generic.ListView):
    model = Task
