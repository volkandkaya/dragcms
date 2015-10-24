# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draggable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('section_type', models.CharField(max_length=1, choices=[('T', 'Title'), ('C', 'Content'), ('Y', 'Youtube'), ('I', 'Image')])),
                ('text', models.TextField(default='')),
                ('section_position', models.IntegerField()),
                ('youtube_width', models.IntegerField(default=560)),
                ('youtube_height', models.IntegerField(default=315)),
                ('image_width', models.IntegerField(default=560)),
                ('image_height', models.IntegerField(default=560)),
                ('visible', models.IntegerField(default=1)),
                ('title_size', models.IntegerField(default=1)),
                ('article_id', models.ForeignKey(to='draggable.Article')),
            ],
        ),
    ]
