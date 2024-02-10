from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','category_image']

class RetailerAdmin(admin.ModelAdmin):
    list_display=['title','image','storefront_image','rating','user']

class ProductImagesAdmin(admin.ModelAdmin):
    model=ProductImages
class ProductAdmin(admin.ModelAdmin):
    inline=[ProductImagesAdmin]
    list_display=['title','image','sale_price','category','retailer','featured','product_status','user']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Retailer,RetailerAdmin)
admin.site.register(ProductImages,ProductImagesAdmin)
admin.site.register(Product,ProductAdmin)