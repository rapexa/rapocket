from json import JSONEncoder
from lib2to3.pgen2 import token
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from web.models import User,Token,Expense,Income
import datetime

# Create your views here.
@csrf_exempt
def submit_income(request):
    """user submit an income"""
    
    #TODO: validate data, user might be fake, token might be fake,amount...
    this_token = request.POST['token']
    this_user = User.objects.filter( token__token = this_token).get()
    
    if 'date' not in request.POST:
        date = datetime.datetime.now()
    
    Income.objects.create(user = this_user, amount=request.POST['amount'],text = request.POST['text'],date=date)
    print("[+] submit income!")
    print(request.POST)
    
    return JsonResponse ({
        'status':'ok',
        
    }, encoder=JSONEncoder)

@csrf_exempt
def submit_expense(request):
    """user submit an expense"""
    
    #TODO: validate data, user might be fake, token might be fake,amount...
    this_token = request.POST['token']
    this_user = User.objects.filter( token__token = this_token).get()
    
    if 'date' not in request.POST:
        date = datetime.datetime.now()
    
    Expense.objects.create(user = this_user, amount=request.POST['amount'],text = request.POST['text'],date=date)
    print("[+] submit expense!")
    print(request.POST)
    
    return JsonResponse ({
        'status':'ok',
        
    }, encoder=JSONEncoder)