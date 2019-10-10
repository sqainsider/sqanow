from django.db import models

# Create your models here.


from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# from django.db import models
from datetime import datetime
# from users.models import CustomUser


# comments ..........

class Choices(models.Model):

    class Meta:
        verbose_name = "Choices List"
        verbose_name_plural = "Choices List"

    name = models.CharField(verbose_name='field', max_length=30, )
    value = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    isActive = models.BooleanField(default=True)
    system = models.CharField(max_length=50, )
    model = models.CharField(max_length=50, blank=True, null=True)
    date_created = models.DateTimeField(
        auto_now=False, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(
    #     CustomUser, related_name='dropdown_createdBy', on_delete=models.CASCADE)
    # lastModified_by = models.ForeignKey(
    #     CustomUser, related_name='dropdown_modifiedBy', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name}:{self.description}"

    # def validation_name(value):
    #     pass

        # if len(value) > 100:
        #     raise ValidationError(_('%(value)s is larger than 10 character'),
        #                           code='invlaid',
        #                           params={'value': value},
        #                           )





# class Company(models.Model):

#     class Meta:
#         verbose_name = "Company"
#         verbose_name_plural = "Companies"

#     name = models.CharField(max_length=10, unique=True)
#     company = models.CharField(max_length=50)
#     description = models.CharField(max_length=30)
#     date_created = models.DateTimeField(
#         auto_now=False, auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#     created_by = models.ForeignKey(
#         CustomUser, related_name='company_createdBy', on_delete=models.CASCADE)
#     lastModified_by = models.ForeignKey(
#         CustomUser, related_name='company_modifiedBy', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.company


# class Project(models.Model):

#     class Meta:
#         verbose_name = "Project"
#         verbose_name_plural = "Projects"

#     name = models.CharField(max_length=10, unique=True)
#     description = models.CharField(max_length=30)
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     start_dt = models.DateField(blank=True, null=True)
#     end_dt = models.DateField(blank=True, null=True)
#     extended_end_dt = models.DateField(blank=True, null=True)
#     date_created = models.DateTimeField(
#         auto_now=False, auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#     created_by = models.ForeignKey(
#         CustomUser, related_name='project_createdBy', on_delete=models.CASCADE)
#     lastModified_by = models.ForeignKey(
#         CustomUser, related_name='project_modifiedBy', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name


