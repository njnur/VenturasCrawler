from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField


from core.models import BaseModel


class Product(BaseModel):
    jan = models.CharField(verbose_name=_('Jan Code'), unique=True, max_length=255)
    product_name = models.TextField(verbose_name=_('Product Name'), null=True, blank=True)
    attributes = models.JSONField(verbose_name=_('Attributes'), null=True, blank=True)
    maker = models.CharField(verbose_name=_('Product Maker'), max_length=255, null=True, blank=True)
    brand = models.CharField(verbose_name=_('Brand'), max_length=255, null=True, blank=True)
    tags_from_description = ArrayField(models.CharField(max_length=100), null=True, blank=True)
    tags_from_review = ArrayField(models.CharField(max_length=100), null=True, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-id']

    def __str__(self):
        return self.product_name
