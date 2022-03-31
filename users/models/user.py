import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from users.models.managers import UserManager
from utils.models import AbstractUUID, AbstractTimeTrackable


class User(AbstractUUID, AbstractBaseUser, PermissionsMixin, AbstractTimeTrackable):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)

    follows = models.ManyToManyField(
        "users.User",
        blank=True,
        related_name=("my_subscribers"),
    )
    subscribers = models.ManyToManyField(
        "users.User",
        blank=True,
        related_name=("my_followers"),
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
