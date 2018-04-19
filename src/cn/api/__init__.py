class AbstractApi(object):
    def __init__(self):
        return super().__init__()

    def get_currencies(self):
        raise NotImplementedError("Subclasses of AbstractApi must provide a "
                                  "get_currencies() method")

    def get_trading_pairs(self):
        raise NotImplementedError("Subclasses of AbstractApi must provide a "
                                  "get_trading_pairs() method")
