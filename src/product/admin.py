from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','sku','description','created_at','updated_at')
    search_fields = ('title','created_at')
admin.site.register( Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id','product','file_path','thumbnail','created_at','updated_at')
    search_fields = ()
admin.site.register(ProductImage, ProductImageAdmin)

class VariantAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','active','created_at','updated_at')
    search_fields = ()
admin.site.register(Variant, VariantAdmin)

class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('id','variant_title','variant','product','created_at','updated_at')
    search_fields = ('variant_title')
admin.site.register(ProductVariant, ProductVariantAdmin)

class ProductVariantPriceAdmin(admin.ModelAdmin):
    list_display = ('product_variant_one','product_variant_two','product_variant_three','price','stock','product','created_at','updated_at')
    search_fields = ('price')
admin.site.register(ProductVariantPrice, ProductVariantPriceAdmin)