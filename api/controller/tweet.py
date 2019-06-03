from django.shortcuts import render
from django.http import HttpResponse
from api.utils.index import error,success,getBody,createToken, verifyToken
# Create your views here.
from django.forms.models  import model_to_dict
import json
from api.models import User,Tweet
from django.views.decorators.csrf import csrf_exempt
import jwt
import datetime


@csrf_exempt
def addTweets(request):
    data = getBody(request)
    isVerified =  verifyToken(data['token'])
    if (isVerified != False):
        u=User.objects.get(id=isVerified['id'])
        t=Tweet(tweettext = data['tweettext'], tweetfile=data['tweetfile'], tweettime = datetime.datetime.now()
        , userId = u
        )
        t.save()
        return success("Tweet Added")
    else:
        return error("Invalid Token")


@csrf_exempt
def getTweets(request):
    data = getBody(request)
    isVerified =  verifyToken(data['token'])
    print(isVerified)
    if (isVerified != False):
        pageStart = (data['index']-1)*10
        pageEnd = data['index']*10 
        totalTweets=Tweet.objects.filter(userId=isVerified['id'])[pageStart:pageEnd]
        tweets =[]
        for t in totalTweets:
            tweets.append(model_to_dict(t))
        print(t)
        return HttpResponse(json.dumps(tweets))
    else:
        return error("Invalid Token")
    