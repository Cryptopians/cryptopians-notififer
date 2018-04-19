from cn.core import handler

exchanges = {}


def add_currencies(exchange_name, currencies=[]):
    """Adds currencies in (memory) store.

    This methos is also responsible for detecting mutations in the store and
    handle further business logic for these mutations, e.g. notifications.
    """
    # Ensure exchange is stored in memory
    if not exchange_name in exchanges:
        exchanges[exchange_name] = {
            'currencies': {},
            'name': exchange_name,
        }
    exchange_currencies = exchanges[exchange_name]['currencies']
    for currency in currencies:
        if not currency['id'] in exchange_currencies:
            # Add new currency in exchange
            exchange_currencies[currency['id']] = currency
            handler.handle_new_currency(exchange_name, currency)
