# Generated by Django 3.0.8 on 2020-07-11 23:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0009_auto_20200712_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='articlecolumn',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
