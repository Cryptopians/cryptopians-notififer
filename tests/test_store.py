from cn.core import handler, store


def test_initialize_store():
    initialized = store.initialize_store()
    assert not initialized


def test_update_store():
    updated = store.update_store()
    assert not updated


def test_reset_state():
    state = store.get_state()
    assert state == {}

    state = store.set_state({'exchange': {}})
    assert state == {'exchange': {}}

    state = store.reset_state()
    assert state == {}


def test_handle_new_market(mocker, exchange):
    mocker.patch.object(handler, 'handle_new_market')
    store.add_markets(exchange, {
        'BTC/USD': {
            'symbol': 'BTC/USD'
        }
    })
    handler.handle_new_market.assert_called_with(exchange, {
        'symbol': 'BTC/USD'
    })
