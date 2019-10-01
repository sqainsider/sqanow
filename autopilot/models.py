from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from datetime import datetime
#from common.models import Company
# from .validations.validation import validation_length
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# from users.models import CustomUser
# from fernet_fields import EncryptedTextField
#from django_cryptography.fields import encrypt
from common.models import Choices


class Elements(models.Model):

    class Meta:
        verbose_name = "Element Repo"
        verbose_name_plural = "Elements Repo"
  
    name = models.CharField(max_length=30)
    label = models.CharField(max_length=50)
    seq = models.IntegerField()
    locator_type = models.ForeignKey(
        Choices, related_name='locator_type', blank=True, null=True, on_delete=models.CASCADE)
    locator = models.CharField(max_length=200, blank=True, null=True)
    # event = models.CharField(choices=ACTION_CHOICES, max_length=20)
    element_type = models.ForeignKey(
        Choices, related_name='element_type', blank=True, null=True, on_delete=models.CASCADE)
    event = models.ForeignKey(
        Choices, related_name='event', blank=True, null=True, on_delete=models.CASCADE)
    default_seq = models.IntegerField()
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    page_feature = models.ForeignKey(
        Feature, related_name='pageFeature', on_delete=models.CASCADE)
    node = models.ForeignKey(
        Feature, related_name='node', on_delete=models.CASCADE)
    system = models.ForeignKey(
        Choices, blank=True, null=True, on_delete=models.CASCADE)
    project = models.CharField(max_length=50)
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    isVerified = models.BooleanField(default=False)
    isActive = models.BooleanField(default=True)
    isScroll = models.BooleanField(default='False')
    date_verified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(
        auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(
    #     CustomUser, related_name='element_createdBy', on_delete=models.CASCADE)
    # lastModified_by = models.ForeignKey(
    #     CustomUser, related_name='element_modifiedBy', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.component}.{self.page_feature}.{self.name}"
        # return self.name

