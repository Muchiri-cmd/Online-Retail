from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','category_image','category_id','id']

class RetailerAdmin(admin.ModelAdmin):
    list_display=['title','retailer_image','rating','user','date']

class ProductImagesAdmin(admin.ModelAdmin):
    model=ProductImages
class ProductAdmin(admin.ModelAdmin):
    inline=[ProductImagesAdmin]
    list_display=['title','product_image','sale_price','category','retailer','featured','product_status']

class ReviewAdmin(admin.ModelAdmin):
    list_display=['product','review','rating','user']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Retailer,RetailerAdmin)
admin.site.register(ProductImages,ProductImagesAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductReview,ReviewAdmin)