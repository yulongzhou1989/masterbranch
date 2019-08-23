rom django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from database.dynamodb.database import Database
from boto3.dynamodb.conditions import Key, Attr
import boto3
import botocore


def login(request):
    m = Member.objects.get(username=request.POST['username'])
    if m.password == request.POST['password']:
        request.session['member_id'] = m.id
        return HttpResponse("You're logged in.")
    else:
        return HttpResponse("Your username and password didn't match.")

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")
