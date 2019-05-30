from django.http import HttpResponse
import json
import jwt
def error(msg):
    err = {
        "success":False,
        "msg":msg
    }
    return HttpResponse(json.dumps(err))
    
def success(msg):
    scs = {
        "success":True,
        "msg":msg
    }
    return HttpResponse(json.dumps(scs))

def getBody(request):
    if (request.method=="POST"):
        try:
            return json.loads(request.body)
        except:
            return False   
    else:
        return False
    
def verifyToken(token):
    try:
        data = jwt.decode(token, 'Rahul@1289', algorithms=['HS256'])
        print(data)
    except:
        print("Invalid token")

def createToken():
    encoded_token = jwt.encode({'user_id': 'abc'}, 'Rahul@1289', algorithm='HS256')
    return encoded_token