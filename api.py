"""
Functions to get currencies from exchangeratesapi.io
"""

from datetime import date, timedelta
from pprint import pprint
from typing import NoReturn

import requests

from currencies_dashboard.settings import API_KEY

REAL_SITE = "https://api.exchangeratesapi.io/api/v1/"
FAKE_SITE = "https://www.docstring.fr/api/rates/"
CURRENCIES = ["USD", "CAD", "EUR", "CNH"]
DURATIONS = {7: "Semaine", 30: "Mois", 365: "Année"}


def get_rates(currencies: list[str], days: int = 30, site: str = FAKE_SITE) -> tuple[list, dict] | NoReturn:
    """
    Get latest rates from specified number of days before today for specified currencies
    """
    end_date = date.today()
    start_date = end_date - timedelta(days=days)
    symbols = ",".join(currencies)
    r = (f"{site}{'timeseries' if site == REAL_SITE else 'history'}"
         f"?start_at={start_date}&end_at={end_date}&symbols={symbols}"
         f"{'&access_key=' + API_KEY if site == REAL_SITE else ''}")
    print(r)
    response = requests.get(r)

    if not response or not response.json():
        raise ConnectionError("Failed to get rates from API")

    api_rates = response.json().get("rates")
    days = [day for day in api_rates.keys()]
    currency_to_rates = {currency: [] for currency in currencies}
    for currency in currency_to_rates:
        for elem in api_rates.values():
            currency_to_rates[currency].append(elem[currency])

    return days, currency_to_rates


if __name__ == '__main__':
    pprint(get_rates(["USD", "EUR"], site=FAKE_SITE))
