from django.contrib import admin
from .models import Products, Category, Orders, Users

# Register your models here.
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description", "img")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "contact", "address")

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ("order_time", "sum", "item_menu_id", "users_id")