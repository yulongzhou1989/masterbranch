from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from database.dynamodb.database import Database
from boto3.dynamodb.conditions import Key, Attr
import boto3
import botocore

def index(request):
    context = {}
    return render(request, 'mysite/index.html', context)

def list(request):
    response = Database.operate('articles', 'scan', '')
    articles = response['Items']
    context = {'articles' : articles}
    return render(request, 'mysite/list.html', context)

def details(request, id=0):
    table = Database.create_table('articles')
    response = table.query(
        KeyConditionExpression=Key('id').eq(id)
    )
    context = {'article' : response['Items'][0]}
    return render(request, 'mysite/detail.html', context)

def save(requset, id=0):
    return HttpResponseRedirect(reverse('mysite:details', args=(id)))
