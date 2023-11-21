import factory

from ..locations.factories import Location


class WeatherReport(factory.django.DjangoModelFactory):
    # TODO: custom faker provider for weather names.
    # https://openweathermap.org/weather-conditions
    name = factory.Sequence(lambda n: f"Weather Report {n}")
    celcius = factory.Sequence(lambda n: n)
    location = factory.SubFactory(Location)

    class Meta:
        model = "weather_reports.WeatherReport"
