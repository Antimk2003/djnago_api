from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product, Order, CustomUser
from django.contrib.auth.admin import UserAdmin
from django import forms

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'total_price', 'status')

# Register custom user
from django.contrib.auth import get_user_model
admin.site.register(get_user_model(), UserAdmin)
