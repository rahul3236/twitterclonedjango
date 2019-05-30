from django.db import models

# Create your models here.
class User(models.Model):
    email=models.EmailField()
    fullname = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    username = models.CharField(max_length=100)
    profilePic = models.CharField(max_length=100, blank=True, null=True)
    verified=models.CharField(max_length=100)

class Tweet(models.Model):
    tweettext=models.CharField( max_length=160)
    tweetfile=models.CharField(max_length=50)
    models.DateTimeField( auto_now=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)