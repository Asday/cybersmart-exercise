from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
        ('completed_tasks', '0002_remove_extra_completed_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedtask',
            name='task',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
        ),
    ]
