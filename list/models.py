import datetime as datetime
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField(max_length=511)
    datetime = models.DateTimeField(auto_now_add=True)
    #deadline = models.DateTimeField(auto_now_add=True, optional=True)
    progress = models.BooleanField(default=False)
    tag = models.ForeignKey(to=Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


