import json

import requests

from cn import settings
from cn.utils.logging import getLogger

logger = getLogger(__name__)


def handle_new_market(exchange, market):
    if settings.SLACK_WEBHOOK_URL:
        # Notify via Slack
        try:
            requests.post(settings.SLACK_WEBHOOK_URL, data=json.dumps({
                'text': 'New market "%s" added to exchange "%s"' % (
                    market['symbol'], exchange.name),
                'username': settings.CN_BOT_NAME,
            }))
        except:
            logger.warning("Couldn't send text message to Slack")

    logger.info("New market '%s' added to exchange '%s'" % (
        market['symbol'], exchange.name))
