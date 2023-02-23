from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

from product.models import Product
from app.models import App
from business.models import Business, BusinessProductConnector

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
        caption =request.data["caption"]
        price =request.data["price"]
        discount = request.data["discount"]
        color = request.data["color"]

        try:
            image = request.FILES["image"]
        except:
            image = None


        try:
            app_user = App.objects.get(auth_code=auth_code)
            product = Product.objects.create(
                caption=caption, 
                price=price,
                discount=discount,
                color=color,
                image=image,
            )
            product.save()

            business = Business.objects.get(id=business_id)
            bp = BusinessProductConnector(business=business, product=product)
            bp.save()

            data = {"detail": "Product added Successfully", "status_lean": True, "product_id": product.id}
            return Response(data)

        except:

            data = {"detail": "Error!!", "status_lean": False}
            return Response(data)

@api_view(['POST'])
def Edit(request):
    if request.method == 'POST':


        auth_code = request.data["auth_code"]
        product_id = request.data["product_id"]
        caption = request.data["caption"]
        price = request.data["price"]
        discount = request.data["discount"]
        color = request.data["color"]


        try:
            app_user = App.objects.get(auth_code=auth_code)
            product = Product.objects.get(id=product_id)

            product.caption = caption
            product.price = price
            product.discount = discount
            product.color = color
            product.save()

            data = {"detail": "Product edited Successfully", "status_lean": True, "product_id": product.id}
            return Response(data)

        except:

            data = {"detail": "Error!!", "status_lean": False}
            return Response(data)



@api_view(['POST'])
def Delete(request):
    if request.method == 'POST':


        auth_code =request.data["auth_code"]
        product_id =request.data["product_id"]


        try:
            app_user = App.objects.get(auth_code=auth_code)
            product = Product.objects.get(id=product_id)

            product.status = False
            product.save()

            data = {"detail": "Product removed Successfully", "status_lean": True, "product_id": product.id}
            return Response(data)

        except:

            data = {"detail": "Error!!", "status_lean": False}
            return Response(data)

