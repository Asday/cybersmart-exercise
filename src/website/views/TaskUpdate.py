from django.views.generic import UpdateView

from tasks.models import Task


class TaskUpdate(UpdateView):
    model = Task
    fields = ["name", "description", "location"]
