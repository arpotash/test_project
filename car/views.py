from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .serializers import OrganizationModelSerializer, CarModelSerializer, CreateUpdateCarModelSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Organization, Car
from rest_framework import generics, status
from .filters import OrganizationNameFilter, CarFilter
# Create your views here.
import logging
log = logging.getLogger('organization_log')


class OrganizationList(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationModelSerializer
    filterset_class = OrganizationNameFilter
    log.info(f'Get {queryset}')


class OrganizationCreate(generics.CreateAPIView):
    serializer_class = OrganizationModelSerializer

    def post(self, request, *args, **kwargs):
        create = self.create(request, *args, **kwargs)
        log.info(f'Organization {create.data} was created')
        return create


class OrganizationDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationModelSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        log.info(f'Organization {instance.name} was deleted')
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        put = self.update(request, *args, **kwargs)
        log.info(f'Organization {instance} was updated')
        return put

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        log.info(f'Get Organization {serializer.data}')
        return Response(serializer.data)


class CarsList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarModelSerializer
    filterset_class = CarFilter
    log.info(f'Get {queryset}')


class CarsCreate(generics.CreateAPIView):
    serializer_class = CreateUpdateCarModelSerializer

    def post(self, request, *args, **kwargs):
        create = self.create(request, *args, **kwargs)
        log.info(f'Car {create.data} was created')
        return create


class CarsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CreateUpdateCarModelSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.in_stock = False
        instance.save()
        log.info(f'Car {instance.name} was deleted')
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        put = self.update(request, *args, **kwargs)
        log.info(f'Car {put.data} was updated')
        return put

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        log.info(f'Get Car {serializer.data}')
        return Response(serializer.data)


