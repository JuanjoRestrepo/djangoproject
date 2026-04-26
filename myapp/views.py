from django.http import HttpResponse, JsonResponse

from .models import Project, Task


# Create your views here.
def index(request):
    return HttpResponse("Index page")


def hello(request, username=None):
    return HttpResponse(f"<h2>Hello {username}!</h2>")


def about(request):
    return HttpResponse("About")


def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)


def tasks(request, task_title=None):
    task = Task.objects.get(title=task_title)
    return HttpResponse(f"Task: {task.title}")
