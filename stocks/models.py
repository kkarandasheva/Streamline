from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    code_2l = models.CharField(max_length=2)
    code_3l = models.CharField(max_length=3)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    web = models.CharField(max_length=200)
    sector = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    employees_count = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"


class Ticker(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tickers"
