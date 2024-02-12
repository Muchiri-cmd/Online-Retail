from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
@login_required
def index_view(request):
   products=Product.objects.filter(featured=True,product_status="published")
   
   context={
      "products":products,
   }
   return render(request,'main/index.html',context)

def category_view(request):
   categories=Category.objects.all()
   context={
      "categories":categories,
   }
   return render(request,"main/categories.html",context)

def category_products_view(request,id):
   category_products=Product.objects.filter(category_id=id)
   context={
      "category_products":category_products,
   }
   return render(request,"main/categorydetails.html",context)

def retailers_view(request):
   retailers=Retailer.objects.all()
   context={
      "retailers":retailers,
   }
   return render(request,"main/retailers.html",context)

def retailer_detail_view(request,id):
   retailers=Retailer.objects.filter(id=id)
   context={
      "retailers":retailers,
   }
   return render(request,"main/retailer_details.html",context)

def all_products_view(request):
   products=Product.objects.filter(product_status="published")
   context={
      "products":products,
   }
   return render(request,"main/products.html",context)