
from django.db import models
from django.utils.functional import cached_property

from ..constants import WEATHER_TO_COLOR


class QuerySet(models.QuerySet):

    def current(self):
        return self.order_by("location", "-when").distinct("location")


class WeatherReport(models.Model):
    name = models.CharField(max_length=200)
    celcius = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.ForeignKey("locations.Location", on_delete=models.PROTECT)
    when = models.DateTimeField(auto_now_add=True, editable=False)

    objects = models.Manager.from_queryset(QuerySet)()

    def __str__(self):
        return f"{self.name} at {self.when}"

    @cached_property
    def as_color(self):
        """
        Returns a string "red", "yellow", or "blue", depending on the
        type of weather nominated in `.name`, or `None` if an unknown
        weather type is nominated.
        """
        return WEATHER_TO_COLOR.get(self.name)
