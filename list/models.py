import datetime as datetime
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField(max_length=511)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    progress = models.BooleanField(default=False)
    tag = models.ManyToManyField(to=Tag, related_name="tasks")

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-progress', 'created']

