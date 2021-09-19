from easypark.serializers import DataSerializer, NetworkSerializer, PlaceSerializer
from easypark.models import Data, Network, Place
from typing import Generic
from django.shortcuts import render
from rest_framework import generics,permissions, serializers ,viewsets,status
# Create your views here.

class AdminNetworkCreate(generics.CreateAPIView):
    queryset=Network.objects.all()
    serializer_class=NetworkSerializer
class DataCreate(generics.CreateAPIView):
    queryset=Data.objects.all()
    serializer_class=DataSerializer
class AdminNodeCreate(generics.CreateAPIView):
    queryset=Data.objects.all()
    serializer_class=DataSerializer
class Reserver(generics.CreateAPIView):
    queryset=Place.objects.all()
    serializer_class=PlaceSerializer



