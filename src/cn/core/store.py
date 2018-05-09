import datetime
import json
import sys

import boto3

from cn import settings
from cn.core import notifications
from cn.utils.logging import getLogger

logger = getLogger(__name__)

s3 = boto3.resource('s3')

_state = {}


def get_state():
    global _state
    return _state


def set_state(value):
    global _state
    _state = value
    return _state


def reset_state():
    global _state
    _state = {}
    return _state


def initialize_store():
    """Initializes initial data for the store.

    Currently this gets a remote json file which is partial updated at runtime
    when new currencies are added per exchange. Primary goal is to keep the
    store persistant, at any kind."""
    try:
        content_object = s3.Object(
            settings.S3_BUCKET_NAME, settings.S3_FILE_NAME)
        file_content = content_object.get()['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)
        set_state(json_content['state'])
    except:
        logger.warning("Couldn't get the specified key from s3")
        return False
    return True


def update_store():
    """Updates data to the persistant store."""
    try:
        content_object = s3.Object(
            settings.S3_BUCKET_NAME, settings.S3_FILE_NAME)
        file_content = json.dumps({
            'last_updated': str(datetime.datetime.utcnow()),
            'state': get_state(),
        })
        content_object.put(ACL='public-read', Body=file_content)
        logger.info("Successfully updated store")
    except:
        logger.warning("Couldn't update the remote store")
        return False
    return True


def add_trading_pair(state, exchange, base_asset, quote_asset, is_new_asset):
    state[exchange.id]['assets'][base_asset].append(quote_asset)
    if not is_new_asset:
        notifications.notify_new_trading_pair(exchange, base_asset, quote_asset)
    logger.info("New trading pair added '%s/%s' on exchange '%s'" % (base_asset, quote_asset, exchange.name))
    return state


def add_asset(state, exchange, base_asset, market):
    state[exchange.id]['assets'][base_asset] = []
    notifications.notify_new_asset(exchange, base_asset, market)
    logger.info("New asset added '%s' on exchange '%s'" % (base_asset, exchange.name))
    return state


def add_exchange(state, exchange):
    state[exchange.id] = {
        'id': exchange.id,
        'name': exchange.name,
        'assets': {},
    }
    notifications.notify_new_exchange(exchange)
    logger.info("New exchange added '%s'" % exchange.name)
    return state


def process_markets(exchange, markets={}):
    """Process markets in (memory) store.

    This method is also responsible for detecting mutations in the store and
    handle further business logic for these mutations, e.g. notifications.
    """
    is_new_exchange = False
    is_new_asset = False

    # Get local state
    state = get_state()

    if not exchange.id in state:
        is_new_exchange = True
        # Add new exchange (e.g. Binance)
        state = add_exchange(state, exchange)

    for market in markets:
        market_base_asset = markets[market]['base']
        market_quote_asset = markets[market]['quote']

        is_new_trading_pair = False

        if not market_base_asset in state[exchange.id]['assets']:
            is_new_asset = True
            # Add new asset (e.g. BTC)
            state = add_asset(state, exchange, market_base_asset, markets)

        if not market_quote_asset in state[exchange.id]['assets'][market_base_asset]:
            is_new_trading_pair = True
            # Add new trading pair (e.g. BTC/USD)
            state = add_trading_pair(state, exchange, market_base_asset, market_quote_asset, is_new_asset)

    # Store local state
    set_state(state)

    return state
