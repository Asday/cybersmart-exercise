from django.db import models


class CompletedTask(models.Model):
    task = models.OneToOneField("tasks.Task", on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f"{self.task_id} completed at {self.when}"
