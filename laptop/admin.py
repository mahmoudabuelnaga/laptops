from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin



admin.site.register(models.Category)
admin.site.register(models.ScreenSize)
admin.site.register(models.Color)
admin.site.register(models.ProcessorFamily)
admin.site.register(models.HardDiskCapacity)
admin.site.register(models.GraphicsCardCapacity)
admin.site.register(models.OperatingSystem)
admin.site.register(models.RAMSize)
admin.site.site_header="Kartona adminstration"

class LaptopAdmin(ImportExportModelAdmin):
    pass
admin.site.register(models.Laptop, LaptopAdmin)

