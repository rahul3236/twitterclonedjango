from django.urls import path

from api.controller import user
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('register', user.register),
    path('login', user.login),
     
    
]