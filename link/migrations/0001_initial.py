# Generated by Django 3.0.8 on 2020-07-10 01:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('avatar', models.ImageField(upload_to='link/')),
                ('url', models.URLField()),
                ('link_time', models.DateTimeField(default=datetime.datetime(2020, 7, 10, 1, 24, 8, 627222, tzinfo=utc))),
            ],
            options={
                'ordering': ('-link_time',),
            },
        ),
    ]
