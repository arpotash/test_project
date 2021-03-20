"""mainapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from car.views import OrganizationList, OrganizationCreate, OrganizationDetails, CarsList, CarsCreate, CarsDetails
from car.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/cars/', CarsList.as_view()),
    path('api/cars/create/', CarsCreate.as_view()),
    path('api/cars/detail/<int:pk>/', CarsDetails.as_view()),
    path('api/organizations/', OrganizationList.as_view()),
    path('api/organizations/create', OrganizationCreate.as_view()),
    path('api/organizations/detail/<int:pk>/', OrganizationDetails.as_view()),
]

urlpatterns += doc_urls

