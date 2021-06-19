from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from django_datetime.datetime import datetime


# from django.utils import timezone


class Example(models.Model):
    date = models.DateField(default=datetime.dnow())
    date_update = models.DateField(blank=True, null=True)
    datetime = models.DateTimeField(default=datetime.dtnow())
    datetime_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "Date: {}".format(self.date)


@receiver(pre_save, sender=Example)
def update(sender, instance, **kwargs):
    if instance is None:
        pass
    else:
        instance.date_update = datetime.dnow(str=True)
        # pass
        # instance.datetime_update = datetime.dtnow(str=True)
