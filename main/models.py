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
     image=models.ImageField(upload_to=user_dir_path)
     description=models.CharField(null=True,max_length=100,blank=True,default="Simply The best")
     rating=models.CharField(max_length=100,default="100")
     contact=models.CharField(max_length=100)
     return_time=models.CharField(max_length=100,default="10")
     address=models.CharField(max_length=100)
     shipping_time=models.CharField(max_length=100)

     #Retailer User model
     user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
     date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
     storefront_image=models.ImageField(upload_to=user_dir_path)

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
    specifications=models.TextField(max_length=100)
    #If product is digital no addressing stuff just email and payment
    digital=models.BooleanField(default=False)

    #User model
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="user_products")

    
    class Meta:
        verbose_name_plural="Products"

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" >' % (self.image.url))
    
    def get_percentage_off(self):
        #Get discounted prices
        discount=((self.base_price-self.sale_price)/self.base_price) * 100
        return discount

class ProductImages(models.Model):
    #Allow addition of multiple images for a product
    images=models.ImageField(upload_to='product-imgs')
    product=models.ForeignKey(Product,null=True,on_delete=models.CASCADE,related_name="product_images")

    class Meta:
        verbose_name_plural="Product Images"
    


    #User model