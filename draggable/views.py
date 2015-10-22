from django.shortcuts import render
from django.utils import timezone
from .models import Article

# Create your views here.
def article_list(request):
    return render(request, 'draggable/article_list.html', {})
