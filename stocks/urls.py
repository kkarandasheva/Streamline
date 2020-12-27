from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('home/', views.home_page, name='home_page'),
    path('home/collection/', views.home_collection, name='home_collection'),
    path('home/tickers/', views.home_tickers, name='home_tickers'),
    path('home/companies/', views.home_companies, name='home_companies'),
    path('home/charts/', views.home_charts, name='home_charts'),
    path('study/', views.study_page, name='study_page'),
    path('analyze/', views.analyze_page, name='analyze_page'),
    path('explore/', views.explore_page, name='explore_page'),
]
