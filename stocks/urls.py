from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticker_list, name='ticker_list'),
]