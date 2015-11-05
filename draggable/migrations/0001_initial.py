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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('visible', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('section_type', models.CharField(max_length=1, choices=[('T', 'Title'), ('C', 'Content'), ('Y', 'Youtube'), ('I', 'Image')])),
                ('text', models.TextField(default='')),
                ('section_position', models.IntegerField()),
                ('width', models.IntegerField(default=560)),
                ('height', models.IntegerField(default=315)),
                ('visible', models.IntegerField(default=1)),
                ('title_size', models.IntegerField(default=1)),
                ('article_id', models.ForeignKey(to='draggable.Article')),
            ],
        ),
    ]
