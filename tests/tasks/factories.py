import factory

from ..locations.factories import Location


class Task(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f"Task {n}")
    location = factory.SubFactory(Location)

    class Meta:
        model = "tasks.Task"
