from django.views.generic import CreateView

from tasks.models import Task


class TaskCreate(CreateView):
    model = Task
    fields = ["name", "description", "location"]
