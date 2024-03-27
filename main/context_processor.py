from main.models import *

def default(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    wishlist=Wishlist.objects.filter(user=request.user).count()
    return{
        'products':products,
        'categories':categories,
        'wishlist':wishlist,
    }