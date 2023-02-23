from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

from product.models import Product
from app.models import App
from wishlist.models import Wishlist
from main.serializers import WishlistSerializer


@api_view(['POST'])
def Add(request):
    if request.method == 'POST':

        auth_code =request.data["auth_code"]
        product_id =request.data["product_id"]

        try:
            owner = App.objects.get(auth_code=auth_code)
            product = Product.objects.get(id=product_id)
            
            wishlist = Wishlist.objects.create(owner=owner, product=product)
            wishlist.save()

            data = {"detail": "Wishlist added Successfully", "status_lean": True, "wishlist_id": wishlist.id}
            return Response(data)

        except:

            data = {"detail": "Error!!", "status_lean": False}
            return Response(data)


@api_view(['GET'])
def All(request, auth_code):
    if request.method == 'GET':
        owner = App.objects.get(auth_code=auth_code)
        wishlists = Wishlist.objects.filter(owner=owner).order_by('-pub_date')

        wishlists_k = []
        for item in wishlists:
            data = {"image": item.product.image.url, "caption": item.product.caption,
            "price": item.product.price, "discount": item.product.discount,
            "color": item.product.color}
            wishlists_k.append(data)

        return Response(wishlists_k)


@api_view(['GET'])
def Get(request, auth_code, wishlist_id):
    if request.method == 'GET':
        owner = App.objects.get(auth_code=auth_code)
        wishlist = Wishlist.objects.get(owner=owner, id=wishlist_id)

        wishlist_k = []
        data = {"image": wishlist.product.image.url, "caption": wishlist.product.caption,
            "price": wishlist.product.price, "discount": wishlist.product.discount,
            "color": wishlist.product.color}

        wishlist_k.append(data)

        return Response(wishlist_k)
