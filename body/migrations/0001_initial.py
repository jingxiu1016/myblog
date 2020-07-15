# Generated by Django 3.0.8 on 2020-07-10 01:24

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(default=datetime.datetime(2020, 7, 10, 1, 24, 8, 607276, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', ckeditor.fields.RichTextField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('views_total', models.PositiveIntegerField(default=0)),
                ('avatar', models.ImageField(blank=True, upload_to='article/%Y/%m/%d/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('column', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article', to='body.ArticleColumn')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
