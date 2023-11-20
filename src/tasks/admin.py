from django.apps import apps
from django.contrib import admin


app_config = apps.get_app_config(__name__.split(".", maxsplit=1)[0])

for model in app_config.get_models():
    admin.site.register(model)
