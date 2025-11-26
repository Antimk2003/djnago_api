from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Category, Product, Order

# -----------------------------
# Category
# -----------------------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

# -----------------------------
# Product
# -----------------------------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'image')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')

# -----------------------------
# Order
# -----------------------------
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'product__name')
    ordering = ('-created_at',)
    readonly_fields = ('total_price', 'created_at', 'updated_at')

# -----------------------------
# Custom User
# -----------------------------
admin.site.register(get_user_model(), UserAdmin)
