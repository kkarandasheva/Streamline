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
from stocks.models import Company, Country
from get_all_tickers import get_tickers as gt
import yfinance as yf


class Command(BaseCommand):
    help = 'Upload list of companies from tickers from get_all_ticker package using yfinance to database (Companies)'

    def handle(self, *args, **kwargs):
        list_of_tickers = gt.get_tickers()
        for tickername in list_of_tickers:
            print(tickername)
            try:
                ticker = yf.Ticker(tickername)

                tags = {'longName': '',
                        'country': '',
                        'website': '',
                        'sector': '',
                        'industry': '',
                        'fullTimeEmployees': 0}

                for tag in tags:
                    try:
                        tags[tag] = ticker.info[tag]
                    except KeyError:
                        pass

                print(tags)

                if tags['longName'] != '':
                    Company.objects.get_or_create(name=tags['longName'],
                                                  country=tags['country'],
                                                  web=tags['website'],
                                                  sector=tags['sector'],
                                                  industry=tags['industry'],
                                                  employees_count=tags['fullTimeEmployees'])
            except:
                pass