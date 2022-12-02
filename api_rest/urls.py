"""api_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers

from chargepoints.views import ChargepointViewsetGet, CustomerViewsetGet
from chargepoints.views import ChargepointViewsetPost, CustomerViewsetPost
from chargepoints.views import ChargepointViewsetDelete, CustomerViewsetDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('chargepoint/get/', ChargepointViewsetGet.as_view()),
    path('chargepoint/get/<int:id>/', ChargepointViewsetGet.as_view()),
    path('chargepoint/post/', ChargepointViewsetPost.as_view()),
    path('chargepoint/delete/<int:id>/', ChargepointViewsetDelete.as_view()),
    path('customers/get/', CustomerViewsetGet.as_view()),
    path('customers/get/<int:id>/', CustomerViewsetGet.as_view()),
    path('customers/post/<int:chargepoint_id>/', CustomerViewsetPost.as_view()),
    path('customers/delete/<int:id>/', CustomerViewsetDelete.as_view()),
]
