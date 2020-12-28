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
from stocks.models import Ticker
from get_all_tickers import get_tickers as gt


class Command(BaseCommand):

    help = 'Upload list of tickers from get_all_ticker package to database (Ticker)'

    def handle(self, *args, **kwargs):
        list_of_tickers = gt.get_tickers()
        for ticker in list_of_tickers:
            Ticker.objects.create(name=ticker)
