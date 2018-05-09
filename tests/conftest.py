import pytest


def pytest_configure(config):
    import sys
    sys._called_from_test = True


def pytest_unconfigure(config):
    import sys
    del sys._called_from_test


@pytest.fixture
def exchange():
    class AttrDict(dict):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__dict__ = self
    return AttrDict({
        'id': 'binance',
        'name': 'Binance'
    })
