from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from model import UserModel, ArticleModel
from django.views.decorators.csrf import csrf_protect
from datetime import datetime
from service import ArticleService
import uuid

def admin_index(request):
    if request.session.get('user_id'):
        return render(request, 'admin/dashboard.html', {})
    else:
        return render(request, 'admin/login.html', {})

@csrf_protect
def admin_login(request):
    user = UserModel.query(request.POST['username']).next()
    if user == None:
        return render(request, 'admin/login.html', {'err_message': 'Wrong username or password!'})
    if user.user_passcode == request.POST['password']:
        request.session['user_id'] = user.user_name
        return redirect('admin_index')
    else:
        return render(request, 'admin/login.html', {'err_message': 'Wrong username or password!'})

def admin_logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass

    return redirect('admin_index')

def admin_list(request, last_evaluated_key=None):
    articles = ArticleService.list(model_name='ArticleModel')
    return render(request, 'admin/list.html', {'articles' : articles['data'], 'lek' : articles['lek']})

def admin_list_pagination(request):

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
        'articles': articles,
        'lek': resp_lek,
    }

    return JsonResponse(data)

def admin_page(request, id=None):
    if id:
        article = ArticleService.getByHashKey('ArticleModel', id)
        return render(request, 'admin/page.html', {'article': article})
    else:
        return render(request, 'admin/page.html', {})

@csrf_protect
def admin_save(request):
    if request.POST['article_id']: # update
        uid = request.POST['article_id']
        article = ArticleModel(id=request.POST['article_id'],title=request.POST['title'])
        try:
            article.update(
                actions=[
                    ArticleModel.category.set(request.POST['category']),
                    ArticleModel.content.set(request.POST['content']),
                ],
                condition=(
                    (ArticleModel.id == request.POST['article_id'])
                )
            )
        except Exception as e:
            print(str(e))
    else: # save
        uid = str(uuid.uuid1())
        article = ArticleModel(id=uid,
                               title=request.POST['title'],
                               category=request.POST['category'],
                               content=request.POST['content'],
                               create_time=str(datetime.now()),
                               editor=request.POST['editor'],
                               tags=request.POST['tags'])
        try:
            article.save()
        except Exception as e:
            print(str(e))

    return redirect('admin_page', id=uid)

@csrf_protect
def admin_search_keyword(request):
    keyword = request.POST['keyword']
    if not keyword:
        return redirect('/admin/mysite/list/')

    articles = ArticleService.searchArticleByKeyword(keyword)
    return render(request, 'admin/list.html', {'articles' : articles['data'], 'lek' : articles['lek']})
