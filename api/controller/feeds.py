from django.shortcuts import render
from django.http import HttpResponse
from api.utils.index import error,success,getBody,createToken, verifyToken
# Create your views here.
from django.forms.models  import model_to_dict
import json
from api.models import User,Tweet, Feeds
from django.views.decorators.csrf import csrf_exempt
import jwt
import feedparser

@csrf_exempt
def addFeeds(request):
    feeds = feedparser.parse('http://rss.cnn.com/rss/edition.rss')
    for f in feeds['entries']:
        #print(f)
        try:
            Feeds.objects.get(link = f['link'])
            print("Feed Found")
        except Feeds.DoesNotExist:
            print("unique ffed")
            try:
                summary = f['summary']
            except:
                summary =None
            try:
                published = f['published']
            except:
                published=None
            try:
                mediaurl = f['media_content'][0]
                mediaurl=mediaurl['url']
                print(mediaurl)
            except:
                mediaurl=None
            link =f['link']
            newfeed = Feeds(title=f['title'],
                    summary=summary,
                    link=link,
                    published=published,
                    media =mediaurl
            )
            newfeed.save()
            print("new fede found")
        
            
    return HttpResponse("dione")


@csrf_exempt
def getFeeds(request):
    data = getBody(request)
    pageStart = (data['index']-1) * 10
    pageEnd = data['index'] * 10
    feeds = Feeds.objects.all()[pageStart:pageEnd]
    jsonfeeds = []
    for f in feeds:
        jsonfeeds.append(model_to_dict(f))
    return HttpResponse(json.dumps(jsonfeeds))