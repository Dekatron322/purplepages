from rest_framework import serializers
from django.contrib.auth.models import User, Group

from business.models import Business
from product.models import Product
from service.models import Service
from blog.models import Blog
from review.models import Review
from app.models import App
from wishlist.models import Wishlist

class StatusSerializer(serializers.Serializer):
    detail = serializers.CharField(max_length=120)
    status_lean = serializers.BooleanField(default=False)
    class Meta:
        #model = Wallet
        fields = ('detail', 'status_lean')


class BlogSerializer(serializers.Serializer):

    class Meta:
        model = Blog
        fields = '__all__'


class WishlistSerializer(serializers.Serializer):

    def get_wishlist(self, instance):
        wishlists = []

        ws = Wishlist.objects.all()
        for item in ws:
            jtem = {
                "product": [{"image": ktem.image, "caption": ktem.caption, "price": ktem.price, "discount": ktem.discount, "color": ktem.color} for ktem in item.comments.all()],
            }

            wishlists.append(jtem)

        return wishlists

    class Meta:
        model = Wishlist
        fields = '__all__'


class BusinessSerializer(serializers.ModelSerializer):
    blogs = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    def get_blogs(self, instance):
        blogs = []

        bs = Blog.objects.all()
        for item in bs:

            jtem = {
                "image": item.image.url,
                "title": item.title,
                "detail": item.detail,
                "comments": [{"comment": ktem.comment, "commenter": ktem.commenter.user.username} for ktem in item.comments.all()],
            }
            blogs.append(jtem)

        return blogs

    def get_services(self, instance):
        services = []

        ss = Service.objects.all()
        for item in ss:
            jtem = {
                "image": item.image.url,
                "title": item.title,
                "detail": item.detail,
            }
            services.append(jtem)

        return services

    def get_products(self, instance):
        products = []

        ps = Product.objects.all()
        for item in ps:
            jtem = {
                "image": item.image.url,
                "caption": item.caption,
                "price": item.price,
                "discount": item.discount,
                "color": item.color,
            }
            products.append(jtem)

        return products

    def get_reviews(self, instance):
        reviews = []

        rs = Review.objects.all()
        
        for item in rs:
            app_user = App.objects.get(user__username=item.username)
            jtem = {
                "username": app_user.user.username,
                "first_name": app_user.first_name,
                "last_name": app_user.last_name,
                "image": app_user.image.url,
                "detail": item.detail,
            }
            reviews.append(jtem)

        return reviews

    class Meta:
        model = Business
        exclude = ("app_user", "status", "auth_code" )
