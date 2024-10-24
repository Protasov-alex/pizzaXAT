from django.contrib import admin
from .models import ItemMenu, Category, Orders, Users

# Register your models here.
admin.site.register(ItemMenu)
admin.site.register(Category)
admin.site.register(Orders)
admin.site.register(Users)