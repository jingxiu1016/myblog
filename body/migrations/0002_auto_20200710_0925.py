# Generated by Django 3.0.8 on 2020-07-10 01:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecolumn',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 10, 1, 25, 4, 426728, tzinfo=utc)),
        ),
    ]
