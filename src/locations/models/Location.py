from decimal import Decimal
from urllib.parse import urlencode

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

import requests


class Location(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(
        max_digits=8,
        decimal_places=6,
        validators=[
            MinValueValidator(Decimal("-90")),
            MaxValueValidator(Decimal("90")),
        ],
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        validators=[
            MinValueValidator(Decimal("-180")),
            MaxValueValidator(Decimal("180")),
        ],
    )

    def __str__(self):
        return self.name

    def get_weather(self):
        """
        Queries the OpenWeather API for current weather data at this
        `Location`.  If successful, creates a `WeatherReport` instance.

        Returns a boolean indicating success.
        """
        params = {
            "lat": self.latitude,
            "lon": self.longitude,
            "units": "metric",
            "appid": settings.OPENWEATHER_API_KEY,
        }
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather"
            f"?{urlencode(params)}",
        )

        if response.status_code != 200:
            # TODO: report issues, API key may need attention.
            return False

        data = response.json()

        name = None
        if "weather" in data:
            if len(data["weather"]):
                if "main" in data["weather"][0]:
                    name = data["weather"][0]["main"]

        celcius = None
        if "main" in data:
            if "temp" in data["main"]:
                celcius = data["main"]["temp"]

        if name is None or celcius is None:
            # TODO: report issues with malformed responses.
            return False

        self.weatherreport_set.create(name=name, celcius=celcius)

        return True
