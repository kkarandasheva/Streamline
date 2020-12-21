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
        return self.code_2l


class Company(models.Model):
    name = models.CharField(max_length=200)
    name_abbr = models.CharField(max_length=4)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    web = models.CharField(max_length=200)
    sector = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    employees_count = models.IntegerField()

    def __str__(self):
        return self.name_abbr
