from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Notes
import json
def notes(request):
    request.params = json.loads(request.body)
    action = request.params['action']
    if action == 'list_notes':
        return listnotes(request)
    elif action == 'add_notes':
        return addnotes(request)
    elif action == 'modify_notes':
        return modifynotes(request)
    elif action == 'del_notes':
        return delnotes(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})

def listnotes(request):
    qs = Notes.objects.values()
    ph = request.params['waste']
    if ph:
        qs = qs.filter(waste=ph)
    retlist = list(qs)
    return JsonResponse({'ret': 0, 'retlist': retlist})

def addnotes(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })
    info = request.params['data']

    # 从请求消息中 获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    record = Notes.objects.create(content=info['content'],
                                 time=info['time'],
                                 waste=info['waste'],
                                 remark=info['remark'])

    return JsonResponse({'ret': 0, 'id': record.id})

def modifynotes(request):

    if ('usertype' not in request.session)and('key' not in request.params):  #request.params['key']用于程序调用此接口，只要在json中加入"key":xxx即可
        return JsonResponse({
            'ret': 302,
           })
    # 从请求消息中 获取修改客户的信息
    # 找到该客户，并且进行修改操作
    notesid = request.params['id']
    newdata = request.params['data']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        note = Notes.objects.get(id=notesid)
    except Notes.DoesNotExist:
        return {
            'ret': 1,
        }
    if 'content' in newdata:
        note.content = newdata['content']
    if 'time' in newdata:
        note.time = newdata['time']
    if 'waste' in newdata:
        note.waste = newdata['waste']
    if 'remark' in newdata:
        note.remark = newdata['remark']

    # 注意，一定要执行save才能将修改信息保存到数据库
    note.save()

    return JsonResponse({'ret': 0})

def delnotes(request):

    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })

    noteid = request.params['id']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        note = Notes.objects.get(id=noteid)
    except Notes.DoesNotExist:
        return {
                'ret': 1,
        }

    # delete 方法就将该记录从数据库中删除了
    note.delete()

    return JsonResponse({'ret': 0})