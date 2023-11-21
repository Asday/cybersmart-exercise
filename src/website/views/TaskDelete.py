from django.urls import reverse_lazy
from django.views.generic import DeleteView

from tasks.models import Task


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy("website:tasks")
