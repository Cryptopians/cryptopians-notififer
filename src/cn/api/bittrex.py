import requests

from cn.api import AbstractApi


class Api(AbstractApi):
    def get_exchange_info(self):
        res = requests.get('https://bittrex.com/api/v1.1/public/getcurrencies')
        return self.deserialize(res.json())

    def deserialize(self, data):
        currencies = []
        for obj in data['result']:
            currencies.append({
                'id': obj['Currency'].upper(),
            })
        return {
            'currencies': currencies,
        }
