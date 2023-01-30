from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

@api_view(['GET'])
def Index(request):
    data = {
    }

    return Response(data)

