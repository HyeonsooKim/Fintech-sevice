from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, name, username, password=None):
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            username=username,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, username, password=None):
        user = self.create_user(
            username=username,
            password=password,
            name=name
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name=_('아이디'),
        max_length=30,
        unique=True,
        blank=False
        )
    name = models.CharField(
        verbose_name=_('이름'),
        max_length=30,
        blank=False
        )
    is_active = models.BooleanField(
    verbose_name=_('Is active'),
    default=True
    )
    date_joined = models.DateTimeField(
    verbose_name=_('Date joined'),
    default=timezone.now
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined',)

    def __str__(self):
        return self.nickname

    def get_full_name(self):        
        return self.nickname

    def get_short_name(self):
        return self.nickname

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All superusers are staff
        return self.is_superuser

    get_full_name.short_description = _('Full name')