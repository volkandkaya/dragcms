from django.shortcuts import render, get_list_or_404
from .models import Article


def article_list(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'draggable/article_list.html', context)


def article_detail(request, pk):
    ordered_article = Article.objects.all()
    articles = get_list_or_404(ordered_article, pk=pk)
    return render(request, 'draggable/article_detail.html', {'articles': articles})


def create_article(request):
    return render(request, 'draggable/create_article.html')
