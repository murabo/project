# coding:utf-8

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
import datetime
from django.core.mail import send_mail

class MyUserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=BaseUserManager.normalize_email(email), username=username, date_of_birth=datetime.date(1981,12,29))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        u = self.create_user(email, password=password)
        u.is_admin = True
        u.save(using=self._db)
        return u

class MyUser(AbstractBaseUser):
    username      = models.CharField(verbose_name=u"ユーザ名", max_length=255)
    email         = models.EmailField(_('email address'), unique=True, blank=True)
    date_of_birth = models.DateField()

    objects = MyUserManager()
    USERNAME_FIELD = 'username'
    # USERNAME_FIELDのフィールドは、必須フィールドに記載してはいけない
    REQUIRED_FIELDS = ['email', 'password']

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    class Meta:
        db_table = 'myuser'
        swappable = 'AUTH_USER_MODEL'