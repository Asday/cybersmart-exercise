from weather_reports.models import WeatherReport


class WeatherReportsMixin:

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "weather_reports": {
                weather_report.location_id: {
                    "celcius": weather_report.celcius,
                    "color": weather_report.as_color,
                }
                for weather_report in WeatherReport.objects.current()
            },
        }
