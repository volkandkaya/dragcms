from django.shortcuts import render, get_object_or_404
from .models import Article


def article_list(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'draggable/article_list.html', context)


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'draggable/article_detail.html', {'article': article})


def create_article(request):
    return render(request, 'draggable/create_article.html')
