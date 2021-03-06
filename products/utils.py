"""Products Utils"""

# Models
from customers.models import Currency


def convert_to_local_currency(currency_abbreviation, USD):
    try:
        currency = Currency.objects.get(abbreviation=currency_abbreviation)
    except Currency.DoesNotExist:
        raise Exception('The currency does not exist.')

    return USD * currency.USD_equivalence
