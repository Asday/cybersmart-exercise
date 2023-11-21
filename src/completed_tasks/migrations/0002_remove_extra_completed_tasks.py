from django.db import migrations


def remove_extra_completed_tasks(apps, schema_editor):
    CompletedTask = apps.get_model(  # noqa: N806
        "completed_tasks.CompletedTask",
    )
    Task = apps.get_model("tasks.Task")  # noqa: N806

    completed_tasks = Task.objects.filter(
        pk__in=CompletedTask.objects.values("task"),
    )

    for task in completed_tasks:
        (
            task.completedtask_set
            .exclude(pk=task.completedtask_set.first().pk)
            .delete()
        )


class Migration(migrations.Migration):

    dependencies = [
        ('completed_tasks', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            remove_extra_completed_tasks,
            migrations.RunPython.noop,
        ),
    ]
