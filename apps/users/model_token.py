from django.db import models


class UserBaseToken(models.Model):
    access_token = models.CharField(max_length=255, unique=True, null=True, default=None, blank=True)
    refresh_token = models.CharField(max_length=255, unique=True, null=True, default=None, blank=True)

    class Meta:
        abstract = True



