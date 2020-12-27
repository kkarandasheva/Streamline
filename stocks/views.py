from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Ticker


@login_required
def home_page(request):
    return render(request, 'stocks/home.html', {})


@login_required
def home_collection(request):
    tickers = Ticker.objects.order_by('name')
    return render(request, 'stocks/home_collection.html', {'tickers': tickers})


@login_required
def home_tickers(request):
    tickers = Ticker.objects.order_by('name')
    return render(request, 'stocks/home_tickers.html', {'tickers': tickers})


@login_required
def study_page(request):
    return render(request, 'stocks/study.html', {})


@login_required
def analyze_page(request):
    return render(request, 'stocks/analyze.html', {})


@login_required
def explore_page(request):
    return render(request, 'stocks/explore.html', {})
