import datetime
import json

import boto3

from cn import settings
from cn.core import handler
from cn.utils.logging import getLogger

logger = getLogger(__name__)

s3 = boto3.resource('s3')

state = {}


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
        state = json_content['state']  # noqa
    except:  # noqa
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
            'state': state,
        })
        content_object.put(ACL='public-read', Body=file_content)
        logger.info("Successfully updated store")
    except:
        logger.warning("Couldn't update the remote store")


def add_markets(exchange, markets=[]):
    """Adds markets in (memory) store.

    This method is also responsible for detecting mutations in the store and
    handle further business logic for these mutations, e.g. notifications.
    """
    is_new_exchange = False
    # Ensure exchange is stored in memory
    if exchange.id not in state:
        state[exchange.id] = {
            'markets': {},
            'id': exchange.id,
            'name': exchange.name,
        }
        is_new_exchange = True
        logger.info("New exchange added '%s'" % exchange.name)
    exchange_markets = state[exchange.id]['markets']
    for market in markets:
        symbol = markets[market]['symbol']
        if not symbol in exchange_markets:
            # Add new market in exchange
            exchange_markets[symbol] = {
                'id': symbol,
            }
            if not is_new_exchange:
                # # Only handle new markets for existing exchanges (prevents
                # # initial handling of all markets)
                handler.handle_new_market(exchange, markets[market])
    state[exchange.id]['markets'] = exchange_markets
