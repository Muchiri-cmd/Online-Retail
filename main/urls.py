from .views import *
from django.urls import path

app_name="main"
urlpatterns = [
    path('',index_view,name="index"),  
    path('categories/',category_view,name="categories"),  
    path('category/<id>',category_products_view,name="categorydetails"),
    path('retailers/',retailers_view,name="retailers"),
    path('retailer/<id>',retailer_detail_view,name="retailerdetails"),
    path('products/',all_products_view,name="products")

]
