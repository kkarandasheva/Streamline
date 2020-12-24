from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('home/', views.home_page, name='home_page'),
    path('home/tickers/', views.home_tickers, name='home_tickers'),
    path('study/', views.study_page, name='study_page'),
    path('analyze/', views.analyze_page, name='analyze_page'),
    path('explore/', views.explore_page, name='explore_page'),
]
