import requests
import random
import string

import os


#############################
url = "http://127.0.0.1:8000/service/add/"
files = {'image': open('/Users/temi/Downloads/dude.png','rb'),
}

data = {
    'auth_code': "6ydpuz18yzy30d95x0ol1on77d0hwvl0",
    'business_id': "2",
    'title': "new service",
    'detail': "new service detail",
}
#############################################

#############################
url = "http://127.0.0.1:8000/blog/add/"
files = {'image': open('/Users/temi/Downloads/dude.png','rb'),
}

data = {
    'auth_code': "6ydpuz18yzy30d95x0ol1on77d0hwvl0",
    'business_id': "2",
    'title': "new blog post",
    'detail': "new bloggg detail",
    'tags': "new,blog,post",
}
#############################################


#############################
#url = "http://127.0.0.1:8000/app/edit-profile/"
#files = {'image': open('/Users/temi/Downloads/dude.png','rb'),
#}

#data = {
#    'auth_code': "6ydpuz18yzy30d95x0ol1on77d0hwvl0",
#    "first_name": "muri",
#	"last_name": "ayo",
#	"phone": "0908765455"
#}
#############################################


r = requests.post(url, files=files, data=data)
print(r.json())


