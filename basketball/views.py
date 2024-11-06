#from django.shortcuts import render

from rest_framework.decorators import api_view #, permission_classes
from rest_framework.response import Response


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/batch/',
        '/net/',
    ]
    return Response(routes)

# Create your views here.
