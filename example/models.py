from django.db import models

from date_time_utils.date_time import DateTime


class Example(models.Model):
    date = models.DateField(default=DateTime('date').now)

    def __str__(self):
        return "Date: {}".format(self.date)
