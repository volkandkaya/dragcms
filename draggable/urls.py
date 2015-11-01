from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.article_list, name='article_list'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.article_detail, name='article_detail'),
    url(r'^article/newarticle$', views.article_new, name='new_article'),
    url(r'^article/(?P<pk>[0-9]+)/edit$', views.article_edit, name='article_edit'),
]
