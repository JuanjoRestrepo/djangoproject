from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Index page")


def hello(request, username=None):
    return HttpResponse(f"<h2>Hello {username}!</h2>")


def about(request):
    return HttpResponse("About")
