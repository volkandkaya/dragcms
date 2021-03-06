from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
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
    width = models.IntegerField(default=560)
    height = models.IntegerField(default=315)
    visible = models.IntegerField(default=1)
    title_size = models.IntegerField(default=1)

    def create_title(dic, pk):
        a = Article.objects.all().filter(pk=pk)[0]
        b = Section(article_id=a, section_type=dic['type'], text=dic['text'],section_position=dic['index'], title_size=1)
        b.save()

    def create_content(dic, pk):
        a = Article.objects.all().filter(pk=pk)[0]
        b = Section(article_id=a, section_type=dic['type'], text=dic['text'],section_position=dic['index'])
        b.save()

    def create_youtube(dic, pk):
        a = Article.objects.all().filter(pk=pk)[0]
        b = Section(article_id=a, section_type=dic['type'], text=dic['url'],section_position=dic['index'], height=dic['height'], width=dic['width'])
        b.save()

    def create_image(dic, pk):
        a = Article.objects.all().filter(pk=pk)[0]
        b = Section(article_id=a, section_type=dic['type'], text=dic['url'],section_position=dic['index'], height=dic['height'], width=dic['width'])
        b.save()


