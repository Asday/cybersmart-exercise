from django.forms.models import modelform_factory

from tasks.models import Task


TaskFormBase = modelform_factory(
    Task,
    fields=["name", "description", "location"],
)


class TaskForm(TaskFormBase):

    class Media:
        js = ["taskForm.js"]

    def __init__(self, *args, **kwargs):
        self.base_fields["location"].widget.template_name = (
            "tasks/fields/location.html"
        )

        super().__init__(*args, **kwargs)
