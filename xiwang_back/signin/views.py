from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
import json
def signin(request):
    userName = request.POST.get('name')
    passWord = request.POST.get('password')
    user = authenticate(username=userName, password=passWord)
    if user is not None:
        request.session['usertype'] = 'hope'
        login(request, user)
        return JsonResponse({'ret': 0})
    # 否则就是用户名、密码有误
    else:
        return JsonResponse({'ret': 1, 'msg': '用户名或者密码错误'})