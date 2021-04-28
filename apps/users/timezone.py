# Modulos nativos de django
from django.conf import settings

# Modulos de python
from datetime import timedelta
import pytz
import datetime

def get_timezone():
    return datetime.datetime.now(tz=pytz.timezone(settings.TIME_ZONE))


def set_time_expired(days=0, minutes=0):
    return get_timezone() + datetime.timedelta(days=days, minutes=minutes)


