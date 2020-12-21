from django.shortcuts import render
from django.utils import timezone
from .models import Ticker

def ticker_list(request):
    tickers = Ticker.objects.order_by('name')
    return render(request, 'stocks/ticker_list.html', {'tickers': tickers})