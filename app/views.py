from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

import string
import random

from app.models import App


def ray_randomiser(length=6):
    landd = string.digits
    return ''.join((random.choice(landd) for i in range(length)))
 

@api_view(['POST'])
def SignUp(request):
    if request.method == 'POST':

        request.session.create()
        auth_code = request.session.session_key

        username =request.data["username"]
        phone =request.data["phone"]
        email =request.data["email"]
        password = request.data["password"]

        try:
            
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()

            app_user = App.objects.create(user=user, first_name="", last_name="",
            phone=phone, auth_code=auth_code, otp_code=ray_randomiser())
            app_user.save()

            data = {"detail": "Enter Otp", "status_lean": True, "auth_code": auth_code}
            return Response(data)

        except:

            data = {"detail": "Error!!", "status_lean": False}
            return Response(data)



@api_view(['POST'])
def SignIn(request):
    if request.method == 'POST':
        username =request.data["username"]
        password = request.data["password"]

        try:

            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    app = App.objects.get(user=user)
                    if app.status == True:
                        data = {"detail": "Successful sign in", "status_lean": True, "auth_code": app.auth_code}
                        return Response(data)

                    else:
                        data = {"detail": "Not successful sign in", "status_lean": False}
                        return Response(data)
                
                else:
                    data = {"detail": "Not successful sign in", "status_lean": False}
                    return Response(data)

            else:
                data = {"detail": "Not successful sign in", "status_lean": False}
                return Response(data)
            

        except:

            data = {"detail": "Not successful sign in", "status_lean": False}
            return Response(data)



@api_view(['POST'])
def Verify(request):
    if request.method == 'POST':

        auth_code = request.data["auth_code"]
        otp_code =request.data["otp_code"]        

        try:
            app = App.objects.get(auth_code=auth_code, otp_code=otp_code)
            if app.otp_code == otp_code:
                app.status = True
                app.save()

                data = {"detail": "Your purple pages account has been successfully created", "status_lean": True}
                return Response(data)

            else:
                data = {"detail": "Verification not successful", "status_lean": False}
                return Response(data)
            

        except:
            data = {"detail": "Verification not successful", "status_lean": False}
            return Response(data)



@api_view(['POST'])
def Reset(request):
    if request.method == 'POST':

        auth_code = request.data["auth_code"]
        password1 = request.data["password1"]
        password2 = request.data["password2"]

        try:
            app = App.objects.get(auth_code=auth_code)
            if app:
                if password1 == password2:
                    user = User.objects.get(app=app)
                    user.set_password(password1)
                    user.save()

                    data = {"detail": "Your password has been successfully reset", "status_lean": True}
                    return Response(data)
                else:
                    data = {"detail": "Reset not successful", "status_lean": False}
                    return Response(data)

            else:
                data = {"detail": "Reset not successful", "status_lean": False}
                return Response(data)

        except:
            data = {"detail": "Reset not successful", "status_lean": False}
            return Response(data)


@api_view(['POST'])
def EditProfile(request):
    if request.method == 'POST':

        auth_code =request.data["auth_code"]
        #username = request.data["username"]
        first_name =request.data["first_name"]
        last_name =request.data["last_name"]
        phone =request.data["phone"]

        try:
            app_user = App.objects.get(auth_code=auth_code)
            app_user.first_name = first_name
            #app_user.username = username
            app_user.last_name = last_name
            app_user.phone = phone
            app_user.save()


            data = {"detail": "Profile Update Successful", "status_lean": True, "auth_code": auth_code}
            return Response(data)

        except:

            data = {"detail": "Error!!", "status_lean": False}
            return Response(data)
