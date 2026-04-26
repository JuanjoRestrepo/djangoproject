from django.urls import path

from .views import about, hello, index

urlpatterns = [
    path("", index),
    path("about/", about),
    path("hello/<str:username>/", hello),
]
