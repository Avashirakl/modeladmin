import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractUUID(models.Model):
    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4(),
                            editable=False,
                            verbose_name=_("Уникальное поле"))

    class Meta:
        abstract = True


class AbstractTimeTrackable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,)

    class Meta:
        abstract = True


class AbstractCreatedByTrackable(models.Model):
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        abstract = True
