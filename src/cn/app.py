import sys
import time

import ccxt

from cn import settings
from cn.core import store
from cn.utils.logging import getLogger
from cn.utils.module import import_string

logger = getLogger(__name__)


def run():
    initialized = store.initialize_store()
    if not initialized:
        logger.warning("Couldn't initialize store from remote")
    while True:
        for exchange in ccxt.exchanges:
            klass = import_string('ccxt.%s' % exchange)
            client = klass()
            if client.has.get('publicAPI'):
                try:
                    markets = client.load_markets()
                except:
                    err = sys.exc_info()[0]
                    msg = "Couldn't fetch data from '%s': %s" % (client.name, err)
                    logger.warning(msg)
                if markets:
                    store.add_markets(client, markets)
        logger.info("Successfully verified data from %d exchanges" % len(clients))  # noqa
        store.update_store()        
        time.sleep(int(settings.CN_INTERVAL))

