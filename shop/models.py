from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserShop(AbstractUser):
    middle_name = models.CharField(_('middle name'), max_length=50, blank=True)
    date_updated = models.DateTimeField(_('date updated'), default=timezone.now)

    def get_full_name(self):
        full_name = '%s %s %s' % (self.last_name, self.first_name, self.last_name)
        return full_name.strip()


class DatingInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ('created',)


class Store(DatingInfo):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class DocumentType(DatingInfo):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class UnitType(DatingInfo):
    name = models.CharField(max_length=200)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(DatingInfo):
    name = models.CharField(max_length=200)
    barcode = models.IntegerField()
    unit = models.ForeignKey(UnitType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Document(DatingInfo):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='documents', on_delete=models.CASCADE)


class DocItem(DatingInfo):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
