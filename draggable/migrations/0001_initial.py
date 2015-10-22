# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('url', models.CharField(max_length=50)),
                ('article_type', models.CharField(choices=[('T', 'Title'), ('C', 'Content'), ('Y', 'Youtube'), ('I', 'Image')], max_length=1)),
                ('piece_position', models.IntegerField()),
                ('youtube_width', models.IntegerField(default=560)),
                ('youtube_height', models.IntegerField(default=315)),
                ('image_width', models.IntegerField(default=560)),
                ('image_height', models.IntegerField(default=560)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('title_size', models.IntegerField(default=1)),
            ],
        ),
    ]
