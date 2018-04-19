import time

from cn import settings
from cn.api.bittrex import Api as BittrexApi
from cn.core import store
from cn.utils.logging import getLogger

logger = getLogger(__name__)


def run():
    while True:
        # Delay
        time.sleep(settings.CN_INTERVAL)
        # Retrieve currency data from exchange(s)
        client = BittrexApi()
        result = client.get_currencies()
        # TODO: Add multiple exchanges and track interval for each
        # Handle new currency data
        store.add_currencies('bittrex', result)
        logger.info("Successfully verified new exchange data")
