#RiverStation admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from OceanData.models import OceanDataModel

# Register your models here.
@admin.register(OceanDataModel)
class OceanDataAdmin(ImportExportModelAdmin):
    pass
