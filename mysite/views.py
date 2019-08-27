from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from model import ArticleModel

LIMIT = 1

def index(request):
    return render(request, 'mysite/index.html', {})

def list(request, last_evaluated_key=None):
    articlesItr = ArticleModel.scan(limit=LIMIT, last_evaluated_key=last_evaluated_key)
    articles = []
    for a in articlesItr:
        lek = articlesItr.last_evaluated_key
        articles.append(a)

    return render(request, 'mysite/list.html', {'articles' : articles, 'lek' : lek})

def list_pagination(request):

    if 'lek_id' in request.GET and request.GET['lek_id']:
        lek = {'id': {'S': request.GET['lek_id']}, 'title': {'S': request.GET['lek_title']}}
    else:
        lek = None
    articlesItr = ArticleModel.scan(limit=LIMIT, last_evaluated_key=lek)
    articles = []
    next_lek = None
    for a in articlesItr:
        next_lek = articlesItr.last_evaluated_key
        articles.append(a._serialize())

    if next_lek == None:
        resp_lek = {'id': '', 'title': ''}
    else:
        resp_lek = {'id': next_lek['id']['S'], 'title': next_lek['title']['S']}

    data = {
        'articles': articles,
        'lek': resp_lek,
    }

    return JsonResponse(data)

def details(request, id=0):
    articleIter = ArticleModel.query(id);
    return render(request, 'mysite/detail.html', {'article' : articleIter.next()})
