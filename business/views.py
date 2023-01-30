from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

from business.models import Business
from app.models import App

@api_view(['GET'])
def Index(request):
    data = {
    }

    return Response(data)




@api_view(['POST'])
def Add(request):
    if request.method == 'POST':


        auth_code =request.data["auth_code"]
        name =request.data["name"]
        business_type = request.data["business_type"]
        rc_number = request.data["rc_number"]
        category =request.data["category"]
        location =request.data["location"]
        description =request.data["description"]
        email =request.data["email"]
        phone =request.data["phone"]
        website = request.data["website"]
        address =request.data["address"]
        marketplace = request.data["marketplace"]
        marketplace_link = request.data["marketplace_link"]


        try:
            app_user = App.objects.get(auth_code=auth_code)

            business = Business.objects.create(
                app_user=app_user, 
                name=name, 
                business_type=business_type, 
                rc_number=rc_number, 
                category=category,
                location=location, 
                description=description, 
                email=email, 
                phone=phone, 
                website=website, 
                address=address, 
                marketplace=marketplace, 
                marketplace_link=marketplace_link)
            business.save()

            data = {"detail": "Business created successfully",
            "status_lean": True, "business_id": business.id}
            return Response(data)

        except:

            data = {"detail": "Error!!", "status_lean": False}
            return Response(data)


@api_view(['POST'])
def Edit(request):
    if request.method == 'POST':

        auth_code =request.data["auth_code"]
        business_id =request.data["business_id"]

        name =request.data["name"]
        business_type = request.data["business_type"]
        rc_number = request.data["rc_number"]
        category =request.data["category"]
        location =request.data["location"]
        description =request.data["description"]
        email =request.data["email"]
        phone =request.data["phone"]
        website = request.data["website"]
        address =request.data["address"]
        marketplace = request.data["marketplace"]
        marketplace_link = request.data["marketplace_link"]


        try:
            app_user = App.objects.get(auth_code=auth_code)

            business = Business.objects.get(id=business_id)
            business.name = name
            business.business_type = business_type
            business.rc_number = rc_number
            business.category = category
            business.location = location
            business.description = description
            business.email = email
            business.phone = phone
            business.website = website
            business.address = address
            business.marketplace = marketplace
            business.marketplace_link = marketplace_link
            business.save()

            data = {"detail": "Business edit successfully",
            "status_lean": True, "business_id": business.id}
            return Response(data)

        except:

            data = {"detail": "Error!!", "status_lean": False}
            return Response(data)





@api_view(['POST'])
def Delete(request):
    if request.method == 'POST':

        auth_code =request.data["auth_code"]
        business_id =request.data["business_id"]

        try:
            app_user = App.objects.get(auth_code=auth_code)

            business = Business.objects.get(id=business_id)
            business.status = False
            business.save()

            data = {"detail": "Business removed successfully",
            "status_lean": True, "business_id": business.id}
            return Response(data)

        except:

            data = {"detail": "Error!!", "status_lean": False}
            return Response(data)


