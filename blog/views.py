from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

from blog.models import Blog, Comment, BlogCommentConnector
from app.models import App
from business.models import Business, BusinessBlogConnector

from main.serializers import BlogSerializer

@api_view(['GET'])
def Index(request):
    if request.method == 'GET':
        blogs = Blog.objects.all().order_by('-pub_date')

        serializer = BlogSerializer(blogs, many=True)
        if serializer:
            return Response(serializer.data)

        else:
            return Response(str("errors!"))



@api_view(['POST'])
def Add(request):
    if request.method == 'POST':


        auth_code =request.data["auth_code"]
        business_id =request.data["business_id"]
        title =request.data["title"]
        detail =request.data["detail"]
        tags =request.data["tags"]

        try:
            image = request.FILES["image"]
        except:
            image = None


        try:
            app_user = App.objects.get(auth_code=auth_code)
            blog = Blog.objects.create(title=title, detail=detail, image=image, tags=tags)
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




@api_view(['POST'])
def AddComment(request):
    if request.method == 'POST':


        auth_code =request.data["auth_code"]
        blog_id =request.data["blog_id"]
        comment =request.data["comment"]

        try:
            commenter = App.objects.get(auth_code=auth_code)
            blog = Blog.objects.get(id=blog_id)

            comment = Comment(commenter=commenter, comment=comment)
            comment.save()

            bc = BlogCommentConnector(blog=blog, comment=comment)
            bc.save()

            data = {"detail": "Comment added Successfully", "status_lean": True, "comment_id": comment.id}
            return Response(data)

        except:

            data = {"detail": "Error!!", "status_lean": False}
            return Response(data)



#@api_view(['GET'])
#def Filter(request, category, location, rating):
#    if request.method == 'GET':
#        blogs = Blog.objects.filter(status=True, category=category, location=location, rating=rating).order_by('-pub_date')

#        serializer = BlogSerializer(blogs, many=True)
 #       if serializer:
  #          return Response(serializer.data)

   #     else:
    #        return Response(str("errors!"))