from django.db import models


class WeatherReport(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey("locations.Location", on_delete=models.PROTECT)
    when = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f"{self.name} at {self.when}"
