from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','category_image','category_id','id']

class RetailerAdmin(admin.ModelAdmin):
    list_display=['title','retailer_image','rating','user','date']


class ProductAdmin(admin.ModelAdmin):
    list_display=['title','product_image','sale_price','category','retailer','featured','product_status']

class ReviewAdmin(admin.ModelAdmin):
    list_display=['product','review','rating','user','date_added']

class OrderAdmin(admin.ModelAdmin):
    list_display=['id','user','order_total_price','date_ordered','name','shipping_address','payment_method','phone']

class CartItemAdmin(admin.ModelAdmin):
    list_display=['order_id','item','image','quantity','price','total']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Retailer,RetailerAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductReview,ReviewAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(CartItem,CartItemAdmin)