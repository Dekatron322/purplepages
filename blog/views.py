from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

from blog.models import Blog
from app.models import App
from business.models import Business, BusinessBlogConnector

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
            app_user = App.objects.get(auth_code=auth_code)
            blog = Blog.objects.create(title=title, detail=detail)
            blog.save()

            business = Business.objects.get(id=business_id)
            bb = BusinessBlogConnector(business=business, blog=blog)
            bb.save()

            data = {"detail": "Blog added Successfully", "status_lean": True, "blog_id": blog.id}
            return Response(data)

        except:

            data = {"detail": "Error!!", "status_lean": False}
            return Response(data)




@api_view(['POST'])
def Edit(request):
    if request.method == 'POST':


        auth_code =request.data["auth_code"]
        blog_id =request.data["blog_id"]
        title =request.data["title"]
        detail =request.data["detail"]


        try:
            app_user = App.objects.get(auth_code=auth_code)
            blog = Blog.objects.get(id=blog_id)

            blog.title = title
            blog.detail = detail
            blog.save()

            data = {"detail": "Blog edited Successfully", "status_lean": True, "blog_id": blog.id}
            return Response(data)

        except:

            data = {"detail": "Error!!", "status_lean": False}
            return Response(data)



@api_view(['POST'])
def Delete(request):
    if request.method == 'POST':


        auth_code =request.data["auth_code"]
        blog_id =request.data["blog_id"]


        try:
            app_user = App.objects.get(auth_code=auth_code)
            blog = Blog.objects.get(id=blog_id)

            blog.status = False
            blog.save()

            data = {"detail": "Blog removed Successfully", "status_lean": True, "blog_id": blog.id}
            return Response(data)

        except:

            data = {"detail": "Error!!", "status_lean": False}
            return Response(data)
