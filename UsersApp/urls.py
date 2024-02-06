from django.urls import path
from.views import *

app_name="UsersApp"
urlpatterns = [
    path("sign-up/",sign_up_view,name="signup"),
    path("sign-in",sign_in_view,name="signin"),
]
