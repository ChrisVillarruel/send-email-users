# Modulos nativos de django
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

# Modulos locales
from .manager import UserManager
from .model_token import UserBaseToken
from .choices import CLIENT, ROLE_CHOICES


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin, UserBaseToken):
    user_id = models.AutoField(auto_created=True, primary_key=True)
    email = models.EmailField(max_length=200, unique=True, null=False, blank=False)
    full_name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=250, null=False, blank=False)
    role = models.CharField(max_length=13, choices=ROLE_CHOICES, default=CLIENT)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'tbl_users'
        ordering = ['-user_id']


    def __str__(self):
        return f'{self.email}'



















