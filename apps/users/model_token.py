from django.db import models


class UserBaseToken(models.Model):
    access_token = models.CharField(max_length=255, unique=True, null=True, default=None)
    refresh_token = models.CharField(max_length=255, unique=True, null=True, default=None)

    class Meta:
        abstract = True



