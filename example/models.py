from django.db import models

from django_datetime.datetime import datetime
# from django.utils import timezone


class Example(models.Model):
    date = models.DateField(default=datetime.dnow())
    datetime = models.DateTimeField(default=datetime.dtnow())

    def __str__(self):
        return "Date: {}".format(self.date)
