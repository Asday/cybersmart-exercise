from django.urls import reverse_lazy
from django.views.generic import UpdateView

from completed_tasks.models import CompletedTask
from tasks.models import Task


class TaskComplete(UpdateView):
    model = Task
    fields = []
    success_url = reverse_lazy("website:tasks")
    template_name_suffix = "_complete"

    def form_valid(self, form):
        CompletedTask.objects.create(task=self.object)

        return super().form_valid(form)
