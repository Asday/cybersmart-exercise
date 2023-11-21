from django.views.generic import UpdateView

from tasks.models import Task

from ..forms import TaskForm

from .mixins import WeatherReportsMixin


class TaskUpdate(WeatherReportsMixin, UpdateView):
    model = Task
    form_class = TaskForm
