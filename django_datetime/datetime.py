# from datetime import datetime
from django.utils import timezone

_t = timezone


class DateTime:
    """ date now """

    @classmethod
    def dnow(cls, str=False):
        if str:
            return _t.datetime.strftime(
                _t.datetime.now(), '%Y-%m-%d'
            )
        else:
            return _t.datetime.now

    """ datetime now """

    @classmethod
    def dtnow(cls, str=False):
        if str:
            return _t.datetime.strftime(
                _t.datetime.now(), '%Y-%m-%d %H:%M:%S'
            )
        else:
            return _t.now


datetime = DateTime()
