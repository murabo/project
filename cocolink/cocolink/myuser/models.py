# coding:utf-8

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class MyUser(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True, blank=True)
    date_of_birth = models.DateField()

    USERNAME_FIELD = 'email'
    # USERNAME_FIELDのフィールドは、必須フィールドに記載してはいけない
    #REQUIRED_FIELDS = ['email']