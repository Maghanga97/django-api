from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
@api_view(["GET"])
def apiOverview(request):
    api_urls = {"Display all users": "/",  
                    "Create users": "/create-user/",
                    "Get all users": "/all-users/", 
                    "Get user":"/user/str:client_no/"}
    return Response(api_urls)

@api_view(["GET"])
def get_all_clients(request):
    clients = Client.objects.all()
    serialized_data = ClientSerializer(clients, many=True)
    return Response(serialized_data.data)

@api_view(["GET"])
def get_user(request, client_no):
    client = Client.objects.get(client_no=client_no)
    serialized_data = ClientSerializer(client, many=True)
    return Response(serialized_data.data)

@api_view(["POST"])
def create_user(request):
    client = ClientSerializer(data=request.data)
    if client.is_valid():
        client.save()
    serialized_data = ClientSerializer(client, many=True)
    return Response(serialized_data.data)
