from datetime import timedelta
import math
import uuid

from django.core.cache import cache
from django.utils import timezone

from celery import shared_task

from locations.models import Location


class InContention(Exception):
    pass


class Idempotent:

    def __init__(self, key):
        self.key = key

    def __enter__(self):
        sentinel = uuid.uuid4()
        response = cache.get_or_set(self.key, sentinel)

        if response != sentinel:
            raise InContention

    def __exit__(self, *args, **kwargs):
        cache.delete(self.key)

        return False


@shared_task
def get_weather():
    try:
        with Idempotent("get_weather_sentinel"):
            calls_per_second = 1
            ttl = math.ceil(1 / calls_per_second / Location.objects.count())

            oldest = timezone.now() - timedelta(seconds=ttl)
            stale = Location.objects.exclude(weatherreport__when__gte=oldest)

            for location in stale:
                get_location_weather.delay(location.pk)

            return f"Started fetching weather for {len(stale)} stale locations."

    except InContention:
        return "Previous `get_weather()` still running."


@shared_task
def get_location_weather(pk):
    try:
        with Idempotent(f"get_location_{pk}_weather_sentinel"):
            if Location.objects.get(pk=pk).get_weather():
                return f"Got weather for `Location({pk})`."
            else:
                return f"Failed to get weather for `Location({pk})`."

    except InContention:
        return f"Previous `get_location_weather({pk})` still running."
