import json

import requests

from cn import settings
from cn.utils.logging import getLogger

logger = getLogger(__name__)


def to_slack(message):
    if settings.SLACK_WEBHOOK_URL:
        try:
            requests.post(settings.SLACK_WEBHOOK_URL, data=json.dumps({
                'text': message,
                'username': settings.CN_BOT_NAME,
            }))
        except:
            logger.warning("Couldn't send text message to Slack")

def notify_new_trading_pair(exchange, base_asset, quote_asset):
    to_slack("New trading pair %s/%s added to %s (%s)" % (
        base_asset,
        quote_asset,
        exchange.name,
        exchange.urls['www'],
    ))


def notify_new_asset(exchange, base_asset, markets):
    pairs = []

    for market in markets:
        if markets[market]['base'] == base_asset:
            pairs.append(markets[market]['quote'])

    to_slack("⚠️ New asset %s added to %s (%s) with pairs %s 🚀🚀🚀" % (
        base_asset,
        exchange.name,
        exchange.urls['www'],
        ", ".join(pairs)
    ))


def notify_new_exchange(exchange):
    to_slack("New exchange %s added (%s) 💱" % (
        exchange.name,
        exchange.urls['www'],
    ))
