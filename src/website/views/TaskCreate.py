from django.views.generic import CreateView

from tasks.models import Task

from ..forms import TaskForm

from .mixins import WeatherReportsMixin


class TaskCreate(WeatherReportsMixin, CreateView):
    model = Task
    form_class = TaskForm
