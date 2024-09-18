from django.db import models

# Create your models here.
class Notes(models.Model):
    # 内容
    content = models.TextField(null=True)

    # 创建日期
    time = models.CharField(max_length=200)

    # 是否放入垃圾桶，1:不放，2:放入
    waste = models.IntegerField()

    # 备注
    remark = models.TextField(null=True)