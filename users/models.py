from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class Account(AbstractBaseUser):
    email = models.EmailField(max_length=60, unique=True, verbose_name='email')
    full_name = models.CharField(max_length=30, unique=True)
    is_instructor = models.BooleanField(default=False)
    date_join = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
