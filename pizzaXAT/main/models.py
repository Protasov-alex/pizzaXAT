from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='main/static/images/')

    def __str__(self):
        return self.name

class Users(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    # img = models.FilePathField(null=True)

    def __str__(self):
        return self.name


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    order_time = models.DateTimeField()
    sum = models.FloatField()
    item_menu = models.ForeignKey(Products, on_delete=models.CASCADE)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
