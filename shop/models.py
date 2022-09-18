from django.db import models
from django.utils import timezone

class Category(models.Model):
    dt      = models.DateTimeField(verbose_name="投稿日時", default=timezone.now)
    name    = models.CharField(verbose_name="カテゴリ名", max_length=10)

    def __str__(self):
        return self.name

    def str_id(self):
        return str(self.id)


class Product(models.Model):
    dt          = models.DateTimeField(verbose_name="投稿日時", default=timezone.now)
    name        = models.CharField(verbose_name="商品名", max_length=50)
    category    = models.ForeignKey(Category, verbose_name="カテゴリ", on_delete=models.CASCADE)
    
    price       = models.IntegerField(verbose_name="価格")
    release     = models.DateField(verbose_name="発売日")
