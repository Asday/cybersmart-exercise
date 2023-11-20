from django.db import models
from django.urls import reverse


class QuerySet(models.QuerySet):

    def open(self):
        return self.filter(completedtask__isnull=True)


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.ForeignKey("locations.Location", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    objects = models.Manager.from_queryset(QuerySet)()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("website:task_detail", kwargs={"pk": self.pk})
