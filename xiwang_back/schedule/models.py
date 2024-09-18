from django.db import models

# Create your models here.
#日程
class Schedule(models.Model):
    #日期
    scheduledata = models.CharField(max_length=200)

    #内容
    content = models.TextField(null=True)

    #是否完成
    finish = models.BooleanField(null=True)

    #备注
    remark = models.TextField(null=True)