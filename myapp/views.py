import logging

from django.http import HttpResponse
from django.shortcuts import render

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
    projects = list(Project.objects.values())
    return render(request, "projects.html", {"projects": projects})


def tasks(request):
    # tasks = list(Task.objects.values())
    task = Task.objects.all()
    return render(request, "tasks.html", {"tasks": task})


def create_task(request):
    form = CreateNewTask(request.POST or None)

    title = request.GET.get("title")
    description = request.GET.get("description")

    # Allow quick creation through URL query params:
    # /create_task/?title=a&description=b
    if title and description:
        project, _ = Project.objects.get_or_create(name="Default Project")
        Task.objects.create(title=title, description=description, project=project)
        logger.info("Task created from query params: %s", title)

    # Standard form submit workflow
    if request.method == "POST" and form.is_valid():
        project, _ = Project.objects.get_or_create(name="Default Project")
        Task.objects.create(
            title=form.cleaned_data["title"],
            description=form.cleaned_data["description"],
            project=project,
        )
        logger.info("Task created from form submit: %s", form.cleaned_data["title"])
        form = CreateNewTask()

    return render(request, "create_task.html", {"form": form})
