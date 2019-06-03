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
    tweettime = models.DateTimeField( auto_now_add=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

class Followers(models.Model):
    userId=models.OneToOneField(User, on_delete=models.CASCADE, related_name="users")
    followerId=models.ManyToManyField(User, related_name="followers")

class Feeds(models.Model):
    title = models.CharField(max_length=1000)
    summary = models.CharField(max_length=2000, blank=True, null=True)
    link = models.CharField(max_length=1000)
    published = models.CharField(max_length=1000, blank=True, null=True)
    media = models.CharField(max_length=1000, blank=True, null=True)
