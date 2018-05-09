from cn.core import notifications, store


def test_initialize_store():
    initialized = store.initialize_store()
    assert not initialized


def test_update_store():
    updated = store.update_store()
    assert not updated


def test_reset_state():
    state = store.get_state()
    assert state == {}

    store.set_state({'exchange': {}})
    assert store.get_state() == {'exchange': {}}

    store.reset_state()
    assert store.get_state() == {}


def test_add_exchange(mocker, exchange):
    mocker.patch.object(store, 'add_exchange')
    store.reset_state()
    store.process_markets(exchange, {
        'BTC/USD': {
            'base': 'BTC',
            'quote': 'USD'
        }
    })
    store.add_exchange.assert_called_once_with({}, exchange)


def test_add_asset(mocker, exchange):
    mocker.patch.object(store, 'add_asset')
    store.reset_state()
    store.process_markets(exchange, {
        'BTC/USD': {
            'base': 'BTC',
            'quote': 'USD'
        }
    },)
    store.add_asset.assert_called_once_with({
        'binance': {
            'id': 'binance',
            'name': 'Binance',
            'assets': {}
        }
    }, exchange, 'BTC', {
        'BTC/USD': {
            'base': 'BTC',
            'quote': 'USD'
        }
    })


def test_add_trading_pair(mocker, exchange):
    mocker.patch.object(store, 'add_trading_pair')
    store.reset_state()
    store.process_markets(exchange, {
        'BTC/USD': {
            'base': 'BTC',
            'quote': 'USD'
        }
    },)
    store.add_trading_pair.assert_called_once_with({
        'binance': {
            'id': 'binance',
            'name': 'Binance',
            'assets': {
                'BTC': []
            }
        }
    }, exchange, 'BTC', 'USD', True)
