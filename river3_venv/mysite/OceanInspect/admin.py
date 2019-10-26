#RiverStation admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from OceanInspect.models import OceanInspectModel


# Register your models here.
@admin.register(OceanInspectModel)

class OceanDataAdmin(ImportExportModelAdmin):
        list_display=('riverName','stationName','riverstationNumber','riverStandard','inspectDate',
        'inspectTime','inspectAirTemp','inspectCMS','inspectWaterTemp','inspectPH','inspectO2','inspectTN',
        'inspectTP','inspectBOD','inspectCOD','inspectSS','inspectCd','inspectPb','inspectCr','inspectNi',
        'inspectCu','inspectZn','inspectMn','inspectEle','inspectCFU','inspectMPN','inspectN2','inspectPSU',
        'inspectNTU','inspectPO34','inspectSixOy','inspectNO3N','inspectNO2N','inspectComment')
