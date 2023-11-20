from django.views.generic import ListView

from tasks.models import Task


class Tasks(ListView):
    queryset = Task.objects.open()
