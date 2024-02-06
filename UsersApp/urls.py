from django.urls import path
from.views import *

app_name="UsersApp"
urlpatterns = [
    path("sign-up/",sign_up_view,name="signup")
]
