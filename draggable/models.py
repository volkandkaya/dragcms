from django.db import models
from django.utils import timezone
# Create your models here.


class Article(models.Model):
    TYPE = (('T', 'Title'), ('C', 'Content'), ('Y', 'Youtube'), ('I', 'Image'))
    url = models.CharField(max_length=50, null=False)
    article_type = models.CharField(max_length=1, choices=TYPE, null=False)
    text = models.TextField(null=False, default="")
    piece_position = models.IntegerField(null=False)
    youtube_width = models.IntegerField(default=560)
    youtube_height = models.IntegerField(default=315)
    image_width = models.IntegerField(default=560)
    image_height = models.IntegerField(default=560)
    visible = models.IntegerField(default=1)
    created_date = models.DateTimeField(
            default=timezone.now)
    title_size = models.IntegerField(default=1)

    def visible(self, n):
        self.visible = n
        self.save()

    def is_visible(self):
        if self.visible > 0:
            return True
        return False
