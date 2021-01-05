from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
import vk 
import random

token="67addbfd34b6c312db9998149a8a379cd0fbf4904f7725d6ce22c0f9f321029970d9bededa00a17b596ba"
session=vk.Session(access_token=token)
vkAPI=vk.API(session)


@csrf_exempt
def index(request):
    body = json.loads(request.body)
    print(body)
    if body == { "type": "confirmation", "group_id": 194135917 }:
        return HttpResponse("eb541d7e")
    if body["type"] == 'message_new':
        user_id = body["object"]["message"]["from_id"]
        msg = body["object"]["message"]["text"]
        vkAPI.messages.send(user_id=user_id, message=msg, random_id=random.randint(1,50000000000000000000000) ,v=5.103)
    return HttpResponse("ok")