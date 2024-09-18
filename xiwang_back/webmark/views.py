from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Webmark
import json
#网址集
def webmark(request):
    request.params = json.loads(request.body)
    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_web':
        return listweb(request)
    elif action == 'add_web':
        return addweb(request)
    elif action == 'modify_web':
        return modifyweb(request)
    elif action == 'del_web':
        return delweb(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})

def listweb(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Webmark.objects.values()

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})

def addweb(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })
    info = request.params['data']

    # 从请求消息中 获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    record = Webmark.objects.create(webname=info['webname'],
                                    weburl=info['weburl'],
                                    remark=info['remark']
                                    )

    return JsonResponse({'ret': 0, 'id': record.id})

def modifyweb(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })
    # 从请求消息中 获取修改客户的信息
    # 找到该客户，并且进行修改操作
    webid = request.params['id']
    newdata = request.params['newdata']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        webmark = Webmark.objects.get(id=webid)
    except Webmark.DoesNotExist:
        return {
            'ret': 1,
        }
    if 'webname' in newdata:
        webmark.webname = newdata['webname']
    if 'weburl' in newdata:
        webmark.weburl = newdata['weburl']
    if 'remark' in newdata:
        webmark.remark = newdata['remark']

    # 注意，一定要执行save才能将修改信息保存到数据库
    webmark.save()
    return JsonResponse({'ret': 0})

def delweb(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })

    info = request.params['id']

    try:
        webmark = Webmark.objects.get(id=info)
    except Webmark.DoesNotExist:
        return JsonResponse({
            'ret': 1,
        })
    webmark.delete()
    return JsonResponse({'ret': 0})