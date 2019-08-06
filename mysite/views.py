from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from database.dynamodb.database import Database

def index(request):
    context = {}
    return render(request, 'mysite/index.html', context)

def list(request):
    response = Database.operate('articles', 'scan', '')
    articles = response['Items']
    context = {'articles' : articles}
    # context = {
    #     'articles': [
    #             {
    #                 'id': '123',
    #                 'title': 'Testing title',
    #                 'category': 'Testing category'
    #             }
    #     ],
    # }

    return render(request, 'mysite/list.html', context)

def details(request, id=0):
    context = {
        'details' : {
            'id': id,
            'title': 'Some title',
            'content': 'Some content',
        }
    }
    return render(request, 'mysite/detail.html', context)
