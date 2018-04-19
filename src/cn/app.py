import time

from cn import settings
from cn.api.bittrex import Api as BittrexApi
from cn.core import store
from cn.utils.logging import getLogger
from cn.utils.module import import_string

logger = getLogger(__name__)


def get_exchange_clients():
    clients = []
    exchanges = settings.CN_EXCHANGES
    for exchange in exchanges:
        klass = import_string('cn.api.%s.Api' % exchange)
        clients.append({
            'exchange': exchange,
            'instance': klass(),
        })
    return clients


def run():
    clients = get_exchange_clients()
    while True:
        time.sleep(settings.CN_INTERVAL)
        for client in clients:
            result = client['instance'].get_exchange_info()
            store.add_currencies(client['exchange'], result['currencies'])
        logger.info("Successfully verified new exchange data")
