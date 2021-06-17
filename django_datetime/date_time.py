from datetime import datetime

_t = datetime


class DateTime:
    """ date now """

    @classmethod
    def dnow(cls):
        return _t.today().date

    """ datetime now """

    @classmethod
    def dtnow(cls):
        return _t.now


datetime = DateTime()
