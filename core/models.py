import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


USER = settings.AUTH_USER_MODEL


class BaseModel(models.Model):
    """
    Base model for all the tables in project
    """

    uid = models.UUIDField(
        verbose_name=_('UUID'),
        unique=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True,
    )
    created_by = models.ForeignKey(
        to=USER,
        verbose_name=_('created by'),
        null=True,
        blank=True,
        related_name='%(class)s_created',
        on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
        editable=False,
        db_index=True
    )
    updated_by = models.ForeignKey(
        to=USER,
        verbose_name=_('updated by'),
        null=True,
        blank=True,
        related_name='%(class)s_updated',
        on_delete=models.SET_NULL
    )
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
