from django.db import models
from django.utils.html import mark_safe
from UsersApp.models import *
from django_ckeditor_5.fields import CKEditor5Field
import uuid

#creates directory structure to store user specific files
STATUS=(
        ("inreview","in Review"),
        ("published","Published"),
        ("disabled","Disabled"),
        ("rejected","Rejected"),
      
)
STOCK_STATUS=(
    ("instock","in Stock"),
    ("outofstock", "Out of Stock"),
)

RATING=(
     (1,"★☆☆☆☆"),
     (2,"★★☆☆☆"),
     (3,"★★★☆☆"),
     (4,"★★★★☆"),
    (5,"★★★★★"),
)

PAYMENT_METHOD=(
    ("dbt","Direct Bank Transfer"),
    ("cod","Cash On Delivery"),
)

def user_dir_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)

class Category(models.Model):
    category_id=models.UUIDField(unique=True,default=uuid.uuid4)
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="category")#define dir within media dir where images stored

    class Meta:
        verbose_name_plural="Categories"

    def category_image(self):
        #Enable img tag to be generated for each category instance and mark string safe for rendering
        #prevents dj template Engine from escaping html while rendering
        return mark_safe('<img src="%s" width="50" height="50">' % (self.image.url))
        
    def __str__(self):
            return self.title
    
class Retailer(models.Model):
     retailer_id=models.UUIDField(unique=True, default=uuid.uuid4)
     title=models.CharField(max_length=100)
     image=models.ImageField(upload_to=user_dir_path,null=True)
     description=models.CharField(null=True,max_length=100,blank=True,default="Simply The best")
     rating=models.CharField(max_length=100,default="100")
     contact=models.CharField(max_length=100)
     return_time=models.CharField(max_length=100,default="10")
     address=models.CharField(max_length=100)
     shipping_time=models.CharField(max_length=100)

     #Retailer User model                                                               
     user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)#on_delete=models.CASCADE,null=False
     date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
     storefront_image=models.ImageField(upload_to=user_dir_path,null=True)

     class Meta:
          verbose_name_plural="Retailers"

     def retailer_image(self):
        return mark_safe('<img src="%s" width="50" height="50" >' % (self.image.url))
     

     def __str__(self):
      return self.title
     
     
class Product(models.Model):
    product_id=models.UUIDField(unique=True, default=uuid.uuid4)
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to=user_dir_path)
    retailer=models.ForeignKey(Retailer,on_delete=models.SET_NULL,null=True,related_name="products")
    description=CKEditor5Field('Text',config_name='default',null="true",blank="True")
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name="category_products")
    base_price=models.DecimalField(max_digits=999999999,decimal_places=2)
    sale_price=models.DecimalField(max_digits=999999999,decimal_places=2)
    stock_status=models.CharField(choices=STOCK_STATUS,max_length=10,default="instock")
    product_status=models.CharField(choices=STATUS,max_length=100,default="inreview")
    warranty_period=models.CharField(max_length=100,default="100")
    featured=models.BooleanField(default=False)
    specifications=models.TextField(max_length=100,null=True,blank=True)
    #If product is digital no addressing stuff just email and payment
    digital=models.BooleanField(default=False)

    #User model
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    
    class Meta:
        verbose_name_plural="Products"

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" >' % (self.image.url))
    
    def get_percentage_off(self):
        #Get discounted prices
        discount=((self.base_price-self.sale_price)/self.base_price) * 100
        return discount
        
class ProductReview(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_reviews")
    review=models.TextField()
    rating=models.IntegerField(choices=RATING,default=None)
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="reviews"

    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating
    
class Order(models.Model):
    order_total_price=models.DecimalField(max_digits=999999999,decimal_places=2)
    date_ordered=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    shipping_address=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    payment_method=models.CharField(max_length=200,choices=PAYMENT_METHOD,default="dbt")
    
    class Meta:
        verbose_name_plural='Cart Orders'

class CartItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    item=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    quantity=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=999999999,decimal_places=2)
    total=models.DecimalField(max_digits=999999999,decimal_places=2)
    invoice_no=models.CharField(max_length=200,null=True)

    def cart_image(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))
    