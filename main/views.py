from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Count,Avg
from .forms import *
from django.template.loader import render_to_string
from decimal import Decimal
from django.contrib import messages

# Create your views here.
@login_required
def index_view(request):
   products=Product.objects.filter(featured=True,product_status="published")
   categories=Category.objects.all()
   context={
      "products":products,
      "categories":categories,
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
   retailer=Retailer.objects.get(id=id)
   products=Product.objects.filter(retailer=retailer)
   context={
      "retailers":retailers,
      "products":products,
   }
   return render(request,"main/retailer_details.html",context)

def all_products_view(request):
   products=Product.objects.filter(product_status="published")
   retailers=Retailer.objects.all()
   context={
      "retailers":retailers,
      "products":products,
   }
   return render(request,"main/products.html",context)

def product_view(request,product_id):
   product=Product.objects.get(id=product_id)
   reviews=ProductReview.objects.filter(product=product).order_by('-date_added')
   rating=ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
   review_form=ReviewForm()
   make_review=True
   if request.user.is_authenticated:
      user_review=ProductReview.objects.filter(user=request.user,product=product).count()
      if user_review>0:
         make_review=False

   context={
      "product":product,
      "reviews":reviews,
      "rating":rating,
      "review_form":review_form,
      "make_review":make_review,
   }
   return render(request,'main/product_detail.html',context)

def make_review(request,product_id):
   product=Product.objects.get(id=product_id)
   
   review=ProductReview.objects.create(
      user=request.user,
      product=product,
      review=request.POST['review'],
      rating=request.POST['rating'],
      
   )
   context={
      'user':request.user.username,
      'review':request.POST['review'],
      'rating':request.POST['rating'],
      
   }
   average_review=ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
   return JsonResponse({
      'bool':True,
      'context':context,
      'average_review':average_review,
   })
     
  
def search_products(request):
    query = request.GET.get("query")
    products = []

    if query:
        products = Product.objects.filter(title__icontains=query) | Product.objects.filter(description__icontains=query)

    context = {
        "query": query,
        "products": products,
    }

    return render(request, 'main/search.html', context)

def search_retailers(request):
    query = request.GET.get("query")
    retailers = []
    if query:
        retailers = Retailer.objects.filter(title__icontains=query)

    context = {
        "query": query,
        "retailers": retailers,
    }

    return render(request, 'main/search_retailers.html', context)

def filter_products(request):
   categories = request.GET.getlist("category[]")
   retailers = request.GET.getlist("retailer[]")
   products=Product.objects.filter(product_status="published").distinct()#more specific
   

   if 'price[]' in request.GET:
      price = Decimal(request.GET.getlist('price[]')[-1])
      products = products.filter(sale_price__lte=price)

   

   if len(retailers)>0:
      products=products.filter(retailer__in=retailers).distinct()
   if len(categories)>0:
      products=products.filter(category__in=categories)

   context={
      "products":products,
   }
   data = render_to_string("main/async/products.html",context)
   return JsonResponse({
        "data":data,

   })

def add_to_cart(request):
   
   cart_product={}

   cart_product[str(request.GET['productId'])]={
      'product_title':request.GET['productTitle'],
      'product_price':request.GET['productPrice'],
      'product_qty':request.GET.get('qty'),
   }

   if 'cart_data_obj' in request.session:
      if str(request.GET['productId']) in request.session['cart_data_obj']:
         cart_data=request.session['cart_data_obj']
         cart_data[str(request.GET['productId'])]['product_qty']=int(cart_product[str(request.GET['productId'])]['product_qty'])
         cart_data.update(cart_data)
         request.session['cart_data_obj']=cart_data
      else:
         cart_data=request.session['cart_data_obj']
         cart_data.update(cart_product)
         request.session['cart_data_obj']=cart_data
   else:
      request.session['cart_data_obj']=cart_product


   return JsonResponse({"data":request.session['cart_data_obj'],'cart_count':len(request.session['cart_data_obj'])})

def view_cart(request):
   cart_total_amount=0
   if 'cart_data_obj' in request.session:
      for product_id,item in request.session['cart_data_obj'].items():
         cart_total_amount+=int(item['product_qty']) * float(item['product_price'])
         return render(request,"main/cart.html",{"cart_data":request.session['cart_data_obj'],'totalcartitems':len(request.session['cart_data_obj']),'cart_total_amount':cart_total_amount})
   else:
      messages.warning(request,"Your cart is empty")
      return redirect("main:index")
