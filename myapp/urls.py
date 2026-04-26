from django.urls import path

from .views import about, hello_world

urlpatterns = [
    path("", hello_world, name="hello_world"),
    path("about/", about, name="about"),
]
