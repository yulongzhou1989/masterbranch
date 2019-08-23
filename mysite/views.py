from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from database.dynamodb.database import Database
from boto3.dynamodb.conditions import Key, Attr
import boto3
import botocore
from model import ArticleModel
#
# import pprint
# pp = pprint.PrettyPrinter(depth=6)

def index(request):
    context = {}
    return render(request, 'mysite/index.html', context)

def list(request, start_from=0):
    articles = ArticleModel.scan(limit=10, last_evaluated_key=start_from)
    context = {'articles' : articles}
    return render(request, 'mysite/list.html', context)

def details(request, id=0):
    itemsIter = ArticleModel.query(id);
    context = {'article' : itemsIter.next()}
    return render(request, 'mysite/detail.html', context)

def save(requset, id=0):
    return HttpResponseRedirect(reverse('mysite:details', args=(id)))
