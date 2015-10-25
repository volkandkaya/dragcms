from django.shortcuts import render, get_list_or_404
from .models import Article, Section


def article_list(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'draggable/article_list.html', context)


def article_detail(request, pk):
    ordered_section= Section.objects.all().order_by('section_position')
    sections = get_list_or_404(ordered_section, article_id = pk)
    return render(request, 'draggable/article_detail.html', {'sections': sections})


def create_article(request):
    return render(request, 'draggable/create_article.html')
