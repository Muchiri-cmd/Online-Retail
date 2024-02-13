from main.models import *

def default(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    return{
        'products':products,
        'categories':categories,
    }