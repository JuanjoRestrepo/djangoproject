from django.urls import path

from .views import about, create_task, hello, index, projects, tasks

urlpatterns = [
    path("", index),
    path("about/", about),
    path("hello/<str:username>/", hello),
    path("projects/", projects),
    path("tasks/", tasks),
    path("create_task/", create_task),
]
