from django.views.generic import ListView

from tasks.models import Task


class Tasks(ListView):
    model = Task
