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
    field_label = models.CharField(max_length=20)
    default_seq = models.IntegerField()
    isActive = models.BooleanField(default=True)
    IsRequired = models.BooleanField(default=True)
    driver = models.CharField(max_length=256)
    element = models.CharField(max_length=256)
    element_locator = models.CharField(max_length=256)
    locator_type = models.ForeignKey(
        Choices, related_name='locator_type', blank=True, null=True, on_delete=models.CASCADE)
    element_method = models.CharField(max_length=100)
    default_value = models.CharField(max_length=100)
    processing = models.CharField(max_length=20)
    sleep = models.IntegerField()
    readonly =  models.BooleanField(default=False)
    derived_field = models.BooleanField(default=True)
    dependency = models.CharField(max_length=20)
    lightning = models.BooleanField(default=False)
    object = models.CharField(max_length=20)
    page = models.CharField(max_length=20)
    isScroll = models.BooleanField(default='False')
    visble = models.BooleanField(default=True)
    special_method = models.CharField(max_length=20)
    validation = models.BooleanField(default=True)
    validation_rule = models.CharField(max_length=20)
    date_created = models.DateTimeField(
        auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(
    #     CustomUser, related_name='element_createdBy', on_delete=models.CASCADE)
    # lastModified_by = models.ForeignKey(
    #     CustomUser, related_name='element_modifiedBy', on_delete=models.CASCADE)


    locator_type = models.ForeignKey(
        Choices, related_name='locator_type', blank=True, null=True, on_delete=models.CASCADE)
    locator = models.CharField(max_length=200, blank=True, null=True)
    # event = models.CharField(choices=ACTION_CHOICES, max_length=20)
    element_type = models.ForeignKey(
        Choices, related_name='element_type', blank=True, null=True, on_delete=models.CASCADE)
    event = models.ForeignKey(
        Choices, related_name='event', blank=True, null=True, on_delete=models.CASCADE)
      # component = models.ForeignKey(Component, on_delete=models.CASCADE)
    # page_feature = models.ForeignKey(
    #     Feature, related_name='pageFeature', on_delete=models.CASCADE)
    # node = models.ForeignKey(
    #     Feature, related_name='node', on_delete=models.CASCADE)
    # system = models.ForeignKey(
    #     Choices, blank=True, null=True, on_delete=models.CASCADE)
    # project = models.CharField(max_length=50)
    # environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    # isVerified = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.component}.{self.page_feature}.{self.name}"
        # return self.name

