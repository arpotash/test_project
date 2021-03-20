from rest_framework import serializers
from .models import Organization, Car


class OrganizationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        exclude = ['uuid']


class CarModelSerializer(serializers.ModelSerializer):
    diller = serializers.StringRelatedField()

    class Meta:
        model = Car
        exclude = ['uuid']


class CreateUpdateCarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ['uuid']