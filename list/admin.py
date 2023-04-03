from django.contrib import admin

from list.models import Task, Tag

# Register your models here.
admin.site.register(Tag)
admin.site.register(Task)
