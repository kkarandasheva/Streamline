"""
This is what needs to be imported
in order to debug this script in isolation
from the rest of the application.
This is probably a bad way.

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Streamline.settings")
import django
django.setup()
"""

from django.core.management.base import BaseCommand, CommandError
from Streamline.settings import *
from stocks.models import Country
import csv

class Command(BaseCommand):

    help = 'Upload data from stocks\management\data\countries.csv to database (Country)'

    def handle(self, *args, **kwargs):
        data_country = os.path.join(BASE_DIR, 'stocks\management\data\countries.csv')
        with open(data_country, newline='') as csvfile:
            next(csvfile)
            filereader = csv.reader(csvfile, delimiter=',')
            for row in filereader:
                Country.objects.create(name=row[0], code_2l=row[1], code_3l=row[2])
