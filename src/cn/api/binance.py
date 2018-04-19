import requests

from cn.api import AbstractApi


class Api(AbstractApi):
    def get_exchange_info(self):
        res = requests.get('https://api.binance.com/api/v1/exchangeInfo')
        return self.deserialize(res.json())

    def deserialize(self, data):
        currencies = []
        for obj in data['symbols']:
            if obj['status'].upper() == 'TRADING':
                currencies.append({
                    'id': obj['baseAsset'].upper(),
                })
        return {
            'currencies': currencies,
        }
