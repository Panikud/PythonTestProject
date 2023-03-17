import requests
import json
from Config import keys

class ConvertionException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        quote_ticker, base_ticker = keys[quote], keys[base]
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = amount * json.loads(r.content)[keys[base]]
        return total_base