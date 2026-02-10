from django.contrib import admin
from django.urls import path
from expenses import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path("",views.register,name='register'),
    path("index",views.index,name="index"),
    path("login", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout",views.cust_logout,name="logout")

    
]
