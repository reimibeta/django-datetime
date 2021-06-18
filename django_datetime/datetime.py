# from datetime import datetime
from django.utils import timezone
_t = timezone


class DateTime:
    """ date now """

    @classmethod
    def dnow(cls):
        return _t.datetime.now

    """ datetime now """

    @classmethod
    def dtnow(cls):
        return _t.now


datetime = DateTime()
