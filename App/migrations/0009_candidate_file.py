# Generated by Django 4.0.2 on 2023-03-24 07:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_alter_candidate_personality'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='file',
            field=models.FileField(default=datetime.datetime(2023, 3, 24, 7, 37, 56, 713469, tzinfo=utc), upload_to=''),
            preserve_default=False,
        ),
    ]