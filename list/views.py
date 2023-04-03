from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from list.models import Task, Tag


# Create your views here.
class TaskListView(generic.ListView):
    model = Task


class TagsListView(generic.ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "list/tags_list.html"


class TagsCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("list:tag-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("list:task-list")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("list:task-list")


def task_undo(request, pk):
    task = Task.objects.get(id=pk)
    task.progress = not task.progress
    task.save()
    return HttpResponseRedirect(reverse_lazy("list:task-list"))
