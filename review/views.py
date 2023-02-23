from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

from app.models import App
from review.models import Review
from business.models import Business, BusinessReviewConnector

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
        username =request.data["username"]
        detail =request.data["detail"]

        try:
            app_user = App.objects.get(auth_code=auth_code)
            review = Review.objects.create(username=username, detail=detail)
            review.save()

            business = Business.objects.get(id=business_id)
            br = BusinessReviewConnector(business=business, review=review)
            br.save()

            data = {"detail": "Review added Successfully", "status_lean": True, "review_id": review.id}
            return Response(data)

        except:

            data = {"detail": "Error!!", "status_lean": False}
            return Response(data)