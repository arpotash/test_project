from uuid import uuid4

from django.db import models

# Create your models here.


class Organization(models.Model):
    Russia = 'Russia'
    USA = 'USA'
    Germany = 'Germany'
    France = 'France'
    Japan = 'Japan'
    countries = [
        (Russia, 'Russia'),
        (USA, 'USA'),
        (Germany, 'Germany'),
        (France, 'France'),
        (Japan, 'Japan'),
    ]
    uuid = models.UUIDField(default=uuid4)
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=32, choices=countries, default='Russia')
    address = models.CharField(max_length=128)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    uuid = models.UUIDField(default=uuid4)
    name = models.CharField(max_length=64)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    in_stock = models.BooleanField(default=True)
    diller = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
