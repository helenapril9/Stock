from django.contrib import admin

from logistic.models import Product, StockProduct, Stock


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'description']

@admin.register(Stock)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','address']


@admin.register(StockProduct)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','quantity', 'price']


