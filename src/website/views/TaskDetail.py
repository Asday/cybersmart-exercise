from django.views.generic import DetailView

from tasks.models import Task


class TaskDetail(DetailView):
    model = Task
