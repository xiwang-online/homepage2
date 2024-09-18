from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Book
import json
def book(request):
    request.params = json.loads(request.body)
    action = request.params['action']
    if action == 'list_book':
        return listbook(request)
    elif action == 'add_book':
        return addbook(request)
    elif action == 'modify_book':
        return modifybook(request)
    elif action == 'del_book':
        return delbook(request)
    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})

def listbook(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Book.objects.values()
    ph = request.params['read']
    if ph:
        qs = qs.filter(read=ph)
    retlist = list(qs)
    return JsonResponse({'ret': 0, 'retlist': retlist})

def addbook(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })
    info = request.params['data']

    # 从请求消息中 获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    record = Book.objects.create(bookname=info['bookname'],
                                 author=info['author'],
                                 readdata=info['readdata'],
                                 wordCount=info['wordCount'],
                                 read=info['read'],
                                 notes=info['notes'],
                                 remark=info['remark'])

    return JsonResponse({'ret': 0, 'id': record.id})

def modifybook(request):

    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })
    # 从请求消息中 获取修改客户的信息
    # 找到该客户，并且进行修改操作
    bookid = request.params['id']
    newdata = request.params['data']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        book = Book.objects.get(id=bookid)
    except Book.DoesNotExist:
        return {
            'ret': 1,
        }
    if 'bookname' in newdata:
        book.bookname = newdata['bookname']
    if 'author' in newdata:
        book.author = newdata['author']
    if 'readdata' in newdata:
        book.readdata = newdata['readdata']
    if 'wordcount' in newdata:
        book.wordCount = newdata['wordcount']
    if 'read' in newdata:
        book.read = newdata['read']
    if 'notes' in newdata:
        book.notes = newdata['notes']
    if 'remark' in newdata:
        book.remark = newdata['remark']

    # 注意，一定要执行save才能将修改信息保存到数据库
    book.save()

    return JsonResponse({'ret': 0})

def delbook(request):

    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
           })

    bookid = request.params['id']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        book = Book.objects.get(id=bookid)
    except Book.DoesNotExist:
        return {
                'ret': 1,
        }

    # delete 方法就将该记录从数据库中删除了
    book.delete()

    return JsonResponse({'ret': 0})