from django.shortcuts import render
from django.http import HttpResponse
from api.utils.index import error,success,getBody,createToken, verifyToken
# Create your views here.
from django.forms.models  import model_to_dict
import json
from api.models import User,Tweet, Followers
from django.views.decorators.csrf import csrf_exempt
import jwt
import datetime

@csrf_exempt
def addFollower(request):
    data = getBody(request)
    u=User(id=data['id'])
    try:
        f=Followers.objects.get(userId=u)
        userToFollow = User.objects.get(id=data['fid'])
        f.followerId.add(userToFollow)
        f.save()
        return success("User exist sop  foloower added")
        
    except Followers.DoesNotExist:
        f=Followers(userId=u)
        f.save()
        userToFollow = User.objects.get(id=data['fid'])
        f.followerId.add(userToFollow)
        f.save()
        return success("New user and new follower added")


@csrf_exempt
def getFollower(request):
    data = getBody(request)
    u=User(id=data['id'])
    try:
        f=Followers.objects.get(userId=u)
        followerList = f.followerId.all()
        print(followerList)
        followers=[]
        for f in followerList:
            followers.append(model_to_dict(f))
        print(followers)
        return HttpResponse(json.dumps(followers))
        
    except Followers.DoesNotExist:
        return HttpResponse(json.dumps([]))




