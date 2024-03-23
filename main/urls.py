from .views import *
from django.urls import path

app_name="main"
urlpatterns = [
    path('',index_view,name="index"),  
    path('categories/',category_view,name="categories"),  
    path('category/<id>/',category_products_view,name="categorydetails"),
    path('retailers/',retailers_view,name="retailers"),
    path('retailer/<id>',retailer_detail_view,name="retailerdetails"),
    path('products/',all_products_view,name="products"),
    path('product/<product_id>',product_view,name="product"),
    path('make-review/<product_id>',make_review,name="makereview"),
    path('search',search_products,name="search"),
    path('search/retailer/',search_retailers,name="searchretailers"),
    path('filter-product/',filter_products, name='filter-product'),
    path('add-to-cart/',add_to_cart,name="add-to-cart"),
    path('cart/',view_cart,name="view-cart")
   

]
