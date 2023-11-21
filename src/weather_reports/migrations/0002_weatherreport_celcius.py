from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherreport',
            name='celcius',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]
