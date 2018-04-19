import requests

from cn.api import AbstractApi


class Api(AbstractApi):
    def get_currencies(self):
        res = requests.get('https://bittrex.com/api/v1.1/public/getcurrencies')
        return self.deserialize_currencies(res.json())

    def deserialize_currencies(self, data):
        result = []
        for obj in data['result']:
            result.append({
                'id': obj['Currency'].lower(),
                'name': obj['CurrencyLong']
            })
        return result
