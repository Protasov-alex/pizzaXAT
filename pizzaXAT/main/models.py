from django.db import models

class ItemMenu(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    img = models.FilePathField()

class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    item_menu = models.ForeignKey(ItemMenu, on_delete=models.CASCADE)

class Orders(models.Model):
    order_time = models.DateTimeField()
    sum = models.FloatField()
    item_menu = models.ForeignKey(ItemMenu, on_delete=models.CASCADE)

class Users(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    img = models.FilePathField()
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE)
