from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from api import get_rates, CURRENCIES, FAKE_SITE, DURATIONS


def dashboard(request: HttpRequest, days_range: int = 30, currencies: str = "USD") -> HttpResponse:
    """View to show currencies charts"""
    days, rates = get_rates(
        currencies=currencies.split(","),
        days=days_range,
        site=FAKE_SITE
    )
    page_label = DURATIONS.get(days_range, "Personnalisé")
    return render(request,
                  'currency/index.html',
                  context={
                      "data": rates,
                      "days_labels": days,
                      "days_range": days_range,
                      "durations": DURATIONS,
                      "page_label": page_label,
                      "currencies": currencies,
                      "ALL_CURRENCIES": CURRENCIES,
                  })


def redirect_index(request: HttpRequest) -> HttpResponse:
    return redirect('home', days_range=30, currencies="USD,EUR")
