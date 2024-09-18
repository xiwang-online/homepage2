from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Excerpt
import json
#摘录
def excerpt(request):
    request.params = json.loads(request.body)
    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_excerpt':
        return listexcerpt(request)
    elif action == 'add_excerpt':
        return addexcerpt(request)
    elif action == 'modify_excerpt':
        return modifyexcerpt(request)
    elif action == 'del_excerpt':
        return delexcerpt(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})

def listexcerpt(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Excerpt.objects.values()

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    retlist = list(qs)

    return JsonResponse({'ret': 0, 'retlist': retlist})

def addexcerpt(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })
    info = request.params['data']

    # 从请求消息中 获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    record = Excerpt.objects.create(content=info['content'],
                                    provenance=info['provenance'],
                                    remark=info['remark']
                                    )

    return JsonResponse({'ret': 0, 'id': record.id})

def modifyexcerpt(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })
    # 从请求消息中 获取修改客户的信息
    # 找到该客户，并且进行修改操作
    excerptid = request.params['id']
    newdata = request.params['newdata']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        excerpt = Excerpt.objects.get(id=excerptid)
    except Excerpt.DoesNotExist:
        return {
            'ret': 1,
        }
    if 'content' in newdata:
        excerpt.content = newdata['content']
    if 'provenance' in newdata:
        excerpt.provenance = newdata['provenance']
    if 'remark' in newdata:
        excerpt.remark = newdata['remark']

    # 注意，一定要执行save才能将修改信息保存到数据库
    excerpt.save()
    return JsonResponse({'ret': 0})

def delexcerpt(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })

    info = request.params['id']

    try:
        excerpt = Excerpt.objects.get(id=info)
    except Excerpt.DoesNotExist:
        return JsonResponse({
            'ret': 1,
        })
    excerpt.delete()
    return JsonResponse({'ret': 0})