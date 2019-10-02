from .models import *
import csv
from django.contrib import admin
from django.http import HttpResponse
from common.toolkits.utils import ExportCVSMixin_Admin
from common.models import Choices


# class CountryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'country')
#     # list_filter = ['system', ]


@admin.register(Choices)
class ChoiceListAdmin(admin.ModelAdmin,  ExportCVSMixin_Admin):
    list_display = ('id', 'name', 'isActive', 'model',  'value', 'description',
                    # 'created_by', 'lastModified_by',
                    'date_created', 'date_updated',)
    # list_filter = ['system', 'name', ]
    # list_filter = ['system', 'name', ]

    search_fields = ('name', 'model',)
    ordering = ('name',)
    exclude = []
    readonly_fields = []
    list_per_page = 10
    actions = ['export_as_csv']


# # admin.site.register(Country, CountryAdmin)
