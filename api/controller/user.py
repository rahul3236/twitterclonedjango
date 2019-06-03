from django.shortcuts import render
from django.http import HttpResponse
from api.utils.index import error,success,getBody,createToken, verifyToken
# Create your views here.
from django.forms.models  import model_to_dict
import json
from api.models import User,Tweet
from django.views.decorators.csrf import csrf_exempt
import jwt

@csrf_exempt
def register(request):
     print(getBody(request))
     u = User(email = 'rkgmil.com', password = "toor", profilePic = None, username = "rahul", verified = False, fullname = "R K oJha")
     u.save()
     print(u.id)

     #return HttpResponse(json.dumps(model_to_dict(u)))
     return createToken({"id":u.id})
     #return success("Successfully Registered")
     
@csrf_exempt

def login(request):
     data = getBody(request)
     data =  verifyToken(data['token'])
     if (data != False):
          print(data)
   
     return HttpResponse(json.dumps(data))
     #return HttpResponse(json.dumps({'toekn':token.decode('utf-8')}))
