from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from model import UserModel, ArticleModel
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect


def admin_index(request):
    if request.session.get('user_id'):
        return render(request, 'admin/dashboard.html', {})
    else:
        return render(request, 'admin/login.html', {})


@csrf_protect
def admin_login(request):
    #if the user is not existed
    try:
        user = UserModel.query(request.POST['username']).next()
    except:
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


def admin_list(request, start_from=0):
    articles = ArticleModel.scan(limit=10, last_evaluated_key=start_from)
    return render(request, 'admin/list.html', {'articles' : articles})
