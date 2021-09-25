"""EasyParking URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from rest_framework.schemas import get_schema_view # new
from rest_framework import permissions # new
from drf_yasg.views import get_schema_view # new
from drf_yasg import openapi # new

schema_view = get_schema_view( # new
    openapi.Info(
        title="easyparking",
        default_version="v1",
        description="All Api to use to Construct easyparking_main",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ngounouloic675@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), # new1
    path('api/user/', include('dj_rest_auth.urls')), # new2
    path('api/user/registration/', include('dj_rest_auth.registration.urls')),#new3
    path('api/easypark/', include('easypark.urls')),

    # path('openapi', name='openapi-schema'),
    path('swagger/', schema_view.with_ui( 'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui( 'redoc', cache_timeout=0), name='schema-redoc'),
]