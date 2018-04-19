class AbstractApi(object):
    def __init__(self):
        return super().__init__()

    def get_exchange_info(self):
        raise NotImplementedError("Subclasses of AbstractApi must provide a "
                                  "get_exchange_info() method")

    def deserialize(self, data):
        return data
