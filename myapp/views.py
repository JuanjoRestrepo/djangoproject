from django.http import HttpResponse
from django.shortcuts import render

from .models import Project


# Create your views here.
def index(request):
    title = "Welcome to my Django App!"
    return render(request, "index.html", {"title": title})


def about(request):
    username = "fazt"
    return render(request, "about.html", {"username": username})


def hello(request, username=None):
    return HttpResponse(f"<h2>Hello {username}!</h2>")


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})


def tasks(request):
    # tasks = list(Task.objects.values())
    return render(request, "tasks.html")
