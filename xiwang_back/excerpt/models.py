from django.db import models

# Create your models here.

#摘录
class Excerpt(models.Model):
    #内容
    content = models.TextField(null=True)
    #出处
    provenance = models.TextField(null=True)
    #备注
    remark = models.TextField(null=True)
