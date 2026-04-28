from django.http import HttpResponse
from django.shortcuts import render

from .models import Project, Task


# Create your views here.
def index(request):
    return render(request, "index.html", {"title": "Welcome to Django App"})


def about(request, username="Juan Restrepo"):
    return render(request, "about.html", {"username": username})


def hello(request, username=None):
    return HttpResponse(f"<h2>Hello {username}!</h2>")


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})


def tasks(request):
    # tasks = list(Task.objects.values())
    task = Task.objects.all()
    return render(request, "tasks.html", {"tasks": task})
