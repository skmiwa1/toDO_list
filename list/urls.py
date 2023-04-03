from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from list.views import TaskListView, TagsListView, TagsCreateView, TagUpdateView, TagDeleteView, TaskUpdateView, \
    TaskDeleteView, TaskCreateView, task_undo

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagsListView.as_view(), name="tag-list"),
    path("tags/create/", TagsCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),

    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),

    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/complete-undo/", task_undo, name="task-undo"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "list"
