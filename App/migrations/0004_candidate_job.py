# Generated by Django 4.0.2 on 2023-03-23 08:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_candidate_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='job',
            field=models.CharField(default=datetime.datetime(2023, 3, 23, 8, 21, 27, 338066, tzinfo=utc), max_length=5),
            preserve_default=False,
        ),
    ]
