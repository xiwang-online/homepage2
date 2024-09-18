from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Schedule
import json
def schedule(request):

    request.params = json.loads(request.body)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_schedule':
        return listschedule(request)
    elif action == 'add_schedule':
        return addschedule(request)
    elif action == 'check_schedule':
        return checkschedule(request)
    elif action == 'del_schedule':
        return delschedule(request)
    elif action =='modify_schedule':
        return modifyschedule(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})

def modifyschedule(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })
    # 从请求消息中 获取修改客户的信息
    # 找到该客户，并且进行修改操作
    scheduleid = request.params['id']
    newdata = request.params['newdata']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        schedule = Schedule.objects.get(id=scheduleid)
    except Schedule.DoesNotExist:
        return {
            'ret': 1,
        }
    if 'remark' in newdata:
        schedule.remark = newdata['remark']

    # 注意，一定要执行save才能将修改信息保存到数据库
    schedule.save()

    return JsonResponse({'ret': 0})

def listschedule(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Schedule.objects.values()
    ph = request.params['time']
    print(ph)
    if ph:
        qs = qs.filter(scheduledata=ph)

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})

def addschedule(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })
    info = request.params['data']
    record = Schedule.objects.create(
        scheduledata=info['time'], content=info['content'], finish=False)
    return JsonResponse({'ret': 0, 'id': record.id})

def checkschedule(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })

    info = request.params['data']

    try:
        todo = Schedule.objects.get(id=info["id"])
    except Schedule.DoesNotExist:
        return JsonResponse({
            'ret': 1,
        })

    todo.finish = bool(1-todo.finish)

    # 注意，一定要执行save才能将修改信息保存到数据库
    todo.save()

    return JsonResponse({'ret': 0})

def delschedule(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })

    info = request.params['data']

    try:
        todo = Schedule.objects.get(id=info["id"])
    except Schedule.DoesNotExist:
        return JsonResponse({
            'ret': 1,
        })
    todo.delete()
    return JsonResponse({'ret': 0})
