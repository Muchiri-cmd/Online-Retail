from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
@login_required
def index_view(request):
   products=Product.objects.all()
   
   context={
      "products":products,
   }
   return render(request,'main/index.html',context)

