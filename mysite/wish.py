from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from model import WishModel
from django.views.decorators.csrf import csrf_protect
from datetime import datetime
from service import WishService
import uuid

def list (request):
    wishes = {}
    if(request.GET.get('top')):
        wishes = WishService.listTopPriorityWishes(top=request.GET.get('top'), status=request.GET.get('status'))
    else:
        wishes = WishService.list(limit=5)

    return render(request, 'admin/wishlist.html', {'wishes' : wishes.get('data'), 'lek' : wishes.get('lek')})

def list_pagination(request):
    print(request)
    if 'lek_id' in request.GET and request.GET['lek_id']:
        lek = {'id': {'S': request.GET['lek_id']}}
    else:
        lek = None

    wishes = WishService.list(last_evaluated_key=lek, limit=5)
    next_lek = wishes['lek']

    if next_lek == None:
        resp_lek = {'id': ''}
    else:
        resp_lek = {'id': next_lek['id']['S']}

    data = {
        'wishes': wishes['data'],
        'lek': resp_lek,
    }

    print(resp_lek)

    return JsonResponse(data)
#

def change_status(request):
    if (request.GET.get('wish_id') and request.GET.get('status')):
        return JsonResponse(WishService.updateStatus(request.GET.get('wish_id'), request.GET.get('status')))

    return JsonResponse({'status': '1'})

def page(request, id=None):
    wish = {}
    if id:
        wish = WishService.getByHashKey('WishModel', id)

    return render(request, 'admin/wish.html', {'wish': wish})

@csrf_protect
def save(request):
    print(request.POST)
    if request.POST.get('wish_id'): # update
        uid = request.POST['wish_id']
        wish = WishModel(id=request.POST['wish_id'])
        try:
            wish.update(
                actions=[
                    WishModel.status.set(request.POST['wish_status']),
                    WishModel.content.set(request.POST['content']),
                    WishModel.priority.set(request.POST['priority']),
                    WishModel.title.set(request.POST['title']),
                    WishModel.timespend.set(request.POST['timespend']),
                    WishModel.finish_time.set(str(datetime.now()) if request.POST['wish_status'] == 'off' else 'On Going')
                ],
                condition=(
                    (WishModel.id == request.POST['wish_id'])
                )
            )
        except Exception as e:
            print(str(e))
    else: # save
        uid = str(uuid.uuid1())
        wish = WishModel(id=uid,
                           status=request.POST['wish_status'],
                           priority=request.POST['priority'],
                           content=request.POST['content'],
                           create_time=str(datetime.now()),
                           timespend=request.POST['timespend'],
                           title=request.POST['title'],
                           parent_wish_id='')
        try:
            wish.save()
        except Exception as e:
            print(str(e))

    return redirect('wish_page', id=uid)
