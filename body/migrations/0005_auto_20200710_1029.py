# Generated by Django 3.0.8 on 2020-07-10 02:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0004_auto_20200710_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecolumn',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 10, 2, 29, 1, 808769, tzinfo=utc)),
        ),
    ]
