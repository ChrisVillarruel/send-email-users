# Modulos nativos de django
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

# Modulos locales
from apps.users.authentication.jwt_token import generate_jwt_token
from apps.users.authentication.get_expired_date_token import get_expired_date_token
from .manager import UserManager
from .model_token import UserBaseToken
from .choices import CLIENT, ROLE_CHOICES, ADMIN
from .timezone import get_timezone



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


    def save(self, *args, **kwargs):
        get_time_now = get_timezone().strftime('%y%m%d')

        
        if self.access_token is None or self.refresh_token is None:
            self.access_token = generate_jwt_token(self.full_name, 'access', self.role, minutes=30)
            self.refresh_token = generate_jwt_token(self.full_name, 'refresh', self.role, days=60)


        if get_time_now >= get_expired_date_token(self.refresh_token):
            self.refresh_token = generate_jwt_token(self.full_name, 'refresh', self.role, days=60)


        if self.is_superuser:
            self.role = ADMIN


        super().save(*args, **kwargs)

















