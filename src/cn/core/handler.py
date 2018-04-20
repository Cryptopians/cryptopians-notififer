import json

import requests

from cn import settings
from cn.utils.logging import getLogger

logger = getLogger(__name__)


def handle_new_currency(exchange_name, currency):
    # Slack
    try:
        requests.post(settings.SLACK_WEBHOOK_URL, data=json.dumps({
            'text': 'New currency %s added to exchange %s' % (
                currency['id'], exchange_name),
            'username': settings.CN_BOT_NAME,
        }))
    except:
        logger.warning("Couldn't send text message to Slack")

    logger.info("New currency '%s' added to exchange '%s'" % (
        currency['id'], exchange_name))
