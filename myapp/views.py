import logging

from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import CreateNewTask
from .models import Project, Task

logger = logging.getLogger(__name__)


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
    return render(request, "projects/projects.html", {"projects": projects})


def tasks(request):
    # tasks = list(Task.objects.values())
    task = Task.objects.all()
    return render(request, "tasks/tasks.html", {"tasks": task})


def create_task(request):
    form = CreateNewTask()
    if request.method == "GET":
        return render(request, "tasks/create_task.html", {"form": form})

    else:
        Task.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            project=Project.objects.get(id=2),
        )
        logger.info("Task created from form submit: %s", request.POST["title"])
        return redirect("/tasks/")
