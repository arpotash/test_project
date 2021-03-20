import json
import os

from django.core.management import BaseCommand
from car.models import Car
from django.utils.crypto import get_random_string
from car.models import Organization, Car

FILE_PATH = 'car/json'


def load_from_json(filename):
    with open(os.path.join(FILE_PATH, filename + '.json'), encoding='utf-8') as json_file:
        return json.load(json_file)


class Command(BaseCommand):
    help = u'Заполнение стартовыми данными'

    def handle(self, *args, **options):
        organizations = load_from_json("organizations")
        Organization.objects.all().delete()
        for organization in organizations:
            Organization.objects.create(**organization)

        cars = load_from_json("cars")
        Car.objects.all().delete()
        for car in cars:
            diller = car['diller']
            _diller = Organization.objects.get(name=diller)
            car['diller'] = _diller
            Car.objects.create(**car)

