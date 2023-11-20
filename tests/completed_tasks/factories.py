import factory

from ..tasks.factories import Task


class CompletedTask(factory.django.DjangoModelFactory):
    task = factory.SubFactory(Task)

    class Meta:
        model = "completed_tasks.CompletedTask"
