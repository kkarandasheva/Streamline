from django.contrib import admin
from .models import Country, Company, Ticker

admin.site.register(Ticker)
admin.site.register(Country)
admin.site.register(Company)

