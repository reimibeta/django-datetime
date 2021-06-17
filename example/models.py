from django.db import models

from django_datetime.datetime import datetime


class Example(models.Model):
    date = models.DateField(default=datetime.dnow())

    def __str__(self):
        return "Date: {}".format(self.date)
