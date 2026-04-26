from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Relationship to Project thru ForeignKey - CASCADE means if a project is deleted, all related tasks will also be deleted
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
