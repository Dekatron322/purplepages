from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

from service.models import Service
from app.models import App
from business.models import Business, BusinessServiceConnector

@api_view(['GET'])
def Index(request):
    data = {
    }

    return Response(data)



@api_view(['POST'])
def Add(request):
    if request.method == 'POST':

        auth_code =request.data["auth_code"]
        business_id =request.data["business_id"]
        title =request.data["title"]
        detail =request.data["detail"]

        try:
            image = request.FILES["image"]
        except:
            image = None


        try:
            app_user = App.objects.get(auth_code=auth_code)
            service = Service.objects.create(title=title, detail=detail, image=image)
            service.save()

            business = Business.objects.get(id=business_id)
            bs = BusinessServiceConnector(business=business, service=service)
            bs.save()

            data = {"detail": "Service added Successfully", "status_lean": True, "service_id": service.id}
            return Response(data)

        except:

            data = {"detail": "Error!!", "status_lean": False}
            return Response(data)




@api_view(['POST'])
def Edit(request):
    if request.method == 'POST':


        auth_code =request.data["auth_code"]
        service_id =request.data["service_id"]
        title =request.data["title"]
        detail =request.data["detail"]

        try:
            image = request.FILES["image"]
        except:
            image = None


        try:
            app_user = App.objects.get(auth_code=auth_code)
            service = Service.objects.get(id=service_id)

            service.image = image
            service.title = title
            service.detail = detail
            service.save()

            data = {"detail": "Service edited Successfully", "status_lean": True, "service_id": service.id}
            return Response(data)

        except:

            data = {"detail": "Error!!", "status_lean": False}
            return Response(data)



@api_view(['POST'])
def Delete(request):
    if request.method == 'POST':


        auth_code =request.data["auth_code"]
        service_id =request.data["service_id"]


        try:
            app_user = App.objects.get(auth_code=auth_code)
            service = Service.objects.get(id=service_id)

            service.status = False
            service.save()

            data = {"detail": "Service removed Successfully", "status_lean": True, "service_id": service.id}
            return Response(data)

        except:

            data = {"detail": "Error!!", "status_lean": False}
            return Response(data)
