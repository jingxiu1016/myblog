# Generated by Django 3.0.8 on 2020-07-11 23:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0008_auto_20200710_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='link_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 11, 23, 4, 46, 791829, tzinfo=utc)),
        ),
    ]
