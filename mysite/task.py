def list (request):
    tasks = {}
    tasks = TaskService.list(limit=6)
    return render(request, 'admin/tasklist.html', {'tasks' : tasks.get('data'), 'lek' : tasks.get('lek')})

def list_pagination(request):
    if 'lek_id' in request.GET and request.GET['lek_id']:
        lek = {'id': {'S': request.GET['lek_id']}}
    else:
        lek = None

    tasks = TaskService.list(last_evaluated_key=lek, limit=5)
    next_lek = tasks['lek']

    if next_lek == None:
        resp_lek = {'id': ''}
    else:
        resp_lek = {'id': next_lek['id']['S']}

    data = {
        'tasks': tasks['data'],
        'lek': resp_lek,
    }

    return JsonResponse(data)

def change_status(request):
    if (request.GET.get('task_id') and request.GET.get('status')):
        return JsonResponse(TaskService.updateStatus(request.GET.get('task_id'), request.GET.get('status')))

    return JsonResponse({'status': '1'})

def page(request, id=None):
    wish = {}
    if id:
        wish = TaskService.getByHashKey('TaskModel', id)

    return render(request, 'admin/task.html', {'task': task})

@csrf_protect
def save(request):
    print(request.POST)
    if request.POST.get('task_id'): # update
        uid = request.POST['task_id']
        wish = TaskModel(id=request.POST['task_id'])
        try:
            wish.update(
                actions=[
                    TaskModel.status.set(request.POST['wish_status']),
                    TaskModel.content.set(request.POST['content']),
                    TaskModel.priority.set(request.POST['priority']),
                    TaskModel.title.set(request.POST['title']),
                    TaskModel.timespend.set(request.POST['timespend']),
                ],
                condition=(
                    (TaskModel.id == request.POST['task_id'])
                )
            )
        except Exception as e:
            print(str(e))
    else: # save
        uid = str(uuid.uuid1())
        wish = TaskModel(id=uid,
                           status=request.POST['wish_status'],
                           priority=request.POST['priority'],
                           content=request.POST['content'],
                           create_time=str(datetime.now()),
                           timespend=request.POST['timespend'],
                           title=request.POST['title'],
                           parent_task_id='')
        try:
            wish.save()
        except Exception as e:
            print(str(e))

    return redirect('task_page', id=uid)
