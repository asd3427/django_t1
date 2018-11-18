from django.db import models

# Create your models here.
class Product(models.Model):
    #标题
    title = models.CharField("产品标题",max_length=20)
    #价格
    pric = models.ImageField("促销价",default=0)
    #分类
    #尺码