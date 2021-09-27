from easypark.serializers import DataSerializer, NetworkSerializer, PlaceSerializer
from easypark.models import Data, Network, Place
from typing import Generic
from easypark.serializers import DataSerializer, NetworkSerializer, PlaceSerializer, NodeSerializer
from easypark.models import Data, Network, Place, Node
from typing import Generic
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics,permissions, serializers ,viewsets,status
from rest_framework import generics, permissions
# new
# Create your views here.

# class AdminNetworkCreate(generics.CreateAPIView):
#     queryset=Network.objects.all()
#     serializer_class=NetworkSerializer
# class DataCreate(generics.CreateAPIView):
#     queryset=Data.objects.all()
#     serializer_class=DataSerializer
# class AdminNodeCreate(generics.CreateAPIView):
#     queryset=Data.objects.all()
#     serializer_class=DataSerializer
# class Reserver(generics.CreateAPIView):
#     queryset=Place.objects.all()
#     serializer_class=PlaceSerializer



class NetworkViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    def list(self, request):
        serializer = NetworkSerializer(Network.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        network = Network.objects.get(id=pk)
        serializer = NetworkSerializer(network)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = NetworkSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        network = Network.objects.get(id=pk)
        serializer = NetworkSerializer(instance=network, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        network = Network.objects.get(id=pk)
        network.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)




class NodeViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    def list(self, request):
        serializer = NodeSerializer(Node.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        node = Node.objects.get(id=pk)
        serializer = NodeSerializer(node)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = NodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        node = Node.objects.get(id=pk)
        serializer = NodeSerializer(instance=node, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        node = Node.objects.get(id=pk)
        node.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)





class DataViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    def list(self, request):
        serializer = DataSerializer(Data.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        data = Data.objects.get(id=pk)
        serializer = NetworkSerializer(data)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = DataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        data = Data.objects.get(id=pk)
        serializer = DataSerializer(instance=data, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        data = Data.objects.get(id=pk)
        data.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)





class PlaceViewSet(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    def list(self, request):
        serializer = PlaceSerializer(Place.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        place = Place.objects.get(id=pk)
        serializer = PlaceSerializer(place)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = PlaceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        place = Place.objects.get(id=pk)
        serializer = PlaceSerializer(instance=place, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        place = Place.objects.get(id=pk)
        place.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



