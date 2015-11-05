from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Article, Section
from .forms import ArticleForm
from django.utils import timezone
from django.shortcuts import redirect
import json
from django.views.decorators.csrf import csrf_exempt

def article_list(request):
    articles = Article.objects.all()
    non_empty_articles = []
    ordered_section = Section.objects.all().order_by('section_position')
    for article in articles:
        try:
            lst = get_list_or_404(ordered_section, article_id=article.pk)
        except:
            lst = []
        if len(lst) > 0:
            non_empty_articles.append(article)
    context = {'articles': non_empty_articles}
    return render(request, 'draggable/article_list.html', context)


def article_detail(request, pk):
    ordered_section = Section.objects.all().order_by('section_position')
    try:
        sections = get_list_or_404(ordered_section, article_id=pk)
    except:
        return redirect('draggable.views.article_list')
    return render(request, 'draggable/article_detail.html', {'sections': sections})


def create_article(request):
    return render(request, 'draggable/create_article.html')


@csrf_exempt
def article_edit(request, pk):
    if request.method == 'POST':
        body = request.body.decode(encoding='UTF-8')
        body = json.loads(body)
        print(body)
        Section.objects.all().filter(article_id=pk).delete()
        for bod in body:
            if bod['type'] == 'T':
                Section.create_title(bod, pk)
            elif bod['type'] == 'Y':
                Section.create_youtube(bod, pk)
            elif bod['type'] == 'I':
                Section.create_image(bod, pk)
            else:
                Section.create_content(bod, pk)
    else:
        try:
            ordered_section = Section.objects.all().order_by('section_position')
            sections = get_list_or_404(ordered_section, article_id=pk)
        except:
            sections = []
        return render(request, 'draggable/article_edit.html', {'sections': sections, 'pk': pk})


def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.created_date = timezone.now()
            article.save()
            return redirect('draggable.views.article_edit', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'draggable/new_article.html', {'form': form})


def article_remove(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('draggable.views.article_list')


def article_admin(request):
    articles = Article.objects.all()
    non_empty_articles = []
    empty_articles = []
    ordered_section = Section.objects.all().order_by('section_position')
    for article in articles:
        try:
            lst = get_list_or_404(ordered_section, article_id=article.pk)
        except:
            lst = []
        if len(lst) > 0:
            non_empty_articles.append(article)
        else:
            empty_articles.append(article)
    context = {'articles': non_empty_articles, 'empty_articles': empty_articles}
    return render(request, 'draggable/article_admin.html', context)
