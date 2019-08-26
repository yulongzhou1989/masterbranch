from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from model import ArticleModel


def index(request):
    return render(request, 'mysite/index.html', {})

def list(request, last_evaluated_key=None):
    articles = ArticleModel.scan(limit=10, last_evaluated_key=last_evaluated_key)
    return render(request, 'mysite/list.html', {'articles' : articles})

def details(request, id=0):
    articleIter = ArticleModel.query(id);
    return render(request, 'mysite/detail.html', {'article' : articleIter.next()})
