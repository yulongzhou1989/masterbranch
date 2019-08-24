from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from model import UserModel
from django.views.decorators.csrf import csrf_protect



def admin_index(request):
    if request.session.get('user_id'):
        return render(request, 'admin/dashboard.html', {})
    else:
        return render(request, 'admin/login.html', {})

@csrf_protect
def admin_login(request):
    user = UserModel.query(request.POST['username']).next()
    print(request.POST['password'])
    if user.user_passcode == request.POST['password']:
        request.session['user_id'] = user.user_name
        return render(request, 'admin/dashboard.html', {})
    else:
        return render(request, 'admin/login.html', {'login_status' : 'Failure'})

def admin_logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")
