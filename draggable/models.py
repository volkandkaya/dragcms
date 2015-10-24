from django.db import models
from django.utils import timezone
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50, null=False)
    created_date = models.DateTimeField(default=timezone.now)
    visible = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class Section(models.Model):
    TYPE = (('T', 'Title'), ('C', 'Content'), ('Y', 'Youtube'), ('I', 'Image'))
    article_id = models.ForeignKey(Article)
    section_type = models.CharField(max_length=1, choices=TYPE, null=False)
    text = models.TextField(null=False, default="")
    section_position = models.IntegerField(null=False)
    youtube_width = models.IntegerField(default=560)
    youtube_height = models.IntegerField(default=315)
    image_width = models.IntegerField(default=560)
    image_height = models.IntegerField(default=560)
    visible = models.IntegerField(default=1)
    title_size = models.IntegerField(default=1)
