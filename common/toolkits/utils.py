import csv
# from django.contrib import admin
from django.http import HttpResponse


class ExportCVSMixin_Admin:

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
            meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field)
                                   for field in field_names])
        return response

    export_as_csv.short_description = "Export Selected item(s)"


# class RunJob:

#     def runjob(self, request, queryset):

#         meta = self.model._meta

#         for job in queryset:
#             job.status = 2
#             job.save()

#         runjob.short.description = "Run Job"
