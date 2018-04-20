import requests

from cn import settings
from cn.api import AbstractApi


class Api(AbstractApi):
    def get_exchange_info(self):
        res = requests.get(settings.CN_DEBUG_ENDPOINT)
        return self.deserialize(res.json())

    def deserialize(self, data):
        currencies = []
        for obj in data['assets']:
            currencies.append({
                'id': obj['id'].upper(),
            })
        return {
            'currencies': currencies,
        }
