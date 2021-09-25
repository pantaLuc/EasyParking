from django.urls import path
from .views import NetworkViewSet, NodeViewSet, DataViewSet, PlaceViewSet


urlpatterns = [
    path("network" , NetworkViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('network/<str:pk>', NetworkViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),

    path("node" , NodeViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('node/<str:pk>', NodeViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),

    path("data" , DataViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('data/<str:pk>', DataViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),

    path("place" , PlaceViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('place/<str:pk>', PlaceViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
]