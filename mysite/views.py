from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from service import ArticleService, TagService, CategoryService
from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request, 'mysite/index.html', {})

def list(request, last_evaluated_key=None):
    articles = ArticleService.list(model_name='ArticleModel')
    cats = CategoryService.list(model_name='CategoryModel', limit=None)
    tags = TagService.list(model_name='TagModel', limit=60)
    return render(request, 'mysite/list.html', {'articles': articles['data'], 'lek': articles['lek'], 'cats': cats['data'], 'tags': tags['data']})

def list_pagination(request):

    if 'lek_id' in request.GET and request.GET['lek_id']:
        lek = {'id': {'S': request.GET['lek_id']}, 'title': {'S': request.GET['lek_title']}}
    else:
        lek = None

    articles = ArticleService.list(model_name='ArticleModel', last_evaluated_key=lek)
    next_lek = articles['lek']
    if next_lek == None:
        resp_lek = {'id': '', 'title': ''}
    else:
        resp_lek = {'id': next_lek['id']['S'], 'title': next_lek['title']['S']}

    data = {
        'articles': articles['data'],
        'lek': resp_lek,
    }

    return JsonResponse(data)

def page(request, id=0):
    article = ArticleService.getByHashKey('ArticleModel', id)
    cats = CategoryService.list(model_name='CategoryModel', limit=None)
    tags = TagService.list(model_name='TagModel', limit=None)
    return render(request, 'mysite/page.html', {'article' : article, 'cats': cats['data'], 'tags': tags['data']})

def list_filter_cat(request, cat=None):
    articles = ArticleService.searchArticleByCat(cat)
    return JsonResponse({'articles': articles['data']})

def list_filter_tag(request, tag=None):
    articles = ArticleService.searchArticleByTag(tag)
    return JsonResponse({'articles': articles['data']})

@csrf_protect
def list_filter_keyword(request):
    keyword = request.POST['keyword']
    if not keyword:
        return redirect('/mysite/list/')

    articles = ArticleService.searchArticleByKeyword(keyword)
    cats = CategoryService.list(model_name='CategoryModel', limit=None)
    tags = TagService.list(model_name='TagModel', limit=60)
    return render(request, 'mysite/list.html', {'articles': articles['data'], 'lek': articles['lek'], 'cats': cats['data'], 'tags': tags['data']})
