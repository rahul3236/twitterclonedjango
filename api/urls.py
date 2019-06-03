from django.urls import path

from api.controller import user,followers
from rest_framework_simplejwt import views as jwt_views
from api.controller import tweet

urlpatterns = [
    path('register', user.register),
    path('login', user.login),
    path('addtweets', tweet.addTweets),
    path('gettweets', tweet.getTweets),
    path('addfollower', followers.addFollower),
    path('getfollower', followers.getFollower)
     
    
]