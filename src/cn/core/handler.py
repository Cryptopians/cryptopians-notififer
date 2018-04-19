from cn.utils.logging import getLogger

logger = getLogger(__name__)


def handle_new_currency(exchange_name, currency):
    # TODO: Send notification(s)
    logger.info("New currency '%s' added to exchange '%s'" % (
        currency['id'], exchange_name))
