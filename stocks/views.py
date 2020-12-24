from django.shortcuts import render
from django.utils import timezone
from .models import Ticker


def home_page(request):
    return render(request, 'stocks/home.html', {})


def home_tickers(request):
    tickers = Ticker.objects.order_by('name')
    return render(request, 'stocks/home_tickers.html', {'tickers': tickers})


def study_page(request):
    return render(request, 'stocks/study.html', {})


def analyze_page(request):
    return render(request, 'stocks/analyze.html', {})


def explore_page(request):
    return render(request, 'stocks/explore.html', {})
