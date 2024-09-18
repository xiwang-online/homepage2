from django.db import models

# Create your models here.
class Webmark(models.Model):
    #网站名
    webname = models.CharField(max_length=200,null=True)
    weburl = models.CharField(max_length=200,null=True)
    #备注
    remark = models.TextField(null=True)

