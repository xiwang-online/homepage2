from django.db import models

# Create your models here.
class Book(models.Model):
    # 书名称
    bookname = models.CharField(max_length=200)

    # 作者
    author = models.CharField(max_length=200)

    # 字数
    wordCount = models.CharField(max_length=200,null=True)

    # 日期
    readdata = models.CharField(max_length=200, null=True)

    # 1:在读、2:未读、3:已读
    read = models.IntegerField(null=True)

    # 评论
    notes = models.TextField(null=True)

    # 备注
    remark = models.TextField(null=True)