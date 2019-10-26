#RiverStation admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ExportActionMixin,ImportExportModelAdmin

from RiverInspect.models import RiverInspectModel
from RiverInspect.models import RiverInspectExport
from RiverInspect.models import RiverInspectExportWQI
# Register your models here.
@admin.register(RiverInspectModel)

class RiverInspectAdmin(ExportActionMixin,ImportExportModelAdmin):
    list_display = ('riverName','stationName','riverstationNumber','riverStandard','inspectDate','inspectTime',
    'inspectAirTemp','inspectCMS','inspectWaterTemp','inspectPH','inspectO2','inspectTN','inspectTP','inspectBOD',
    'inspectCOD','inspectSS','inspectCd','inspectPb','inspectCr','inspectNi','inspectCu','inspectZn','inspectMn',
    'inspectEle','inspectCFU','inspectAnionic','inspectN2','inpectOrgC','inspectPers','inspectOil','inspectNTU',
    'inspectNO3N','inspectNO2N','inspectComment')

@admin.register(RiverInspectExport)

class RiverInspectExportAdmin(ExportActionMixin,ImportExportModelAdmin):
        list_display=('stationName','inspectO2','inspectBOD','inspectSS','inspectN2','RPI_Point','RPI_Result')

@admin.register(RiverInspectExportWQI)
class RiverInspectExportWQIAdmin(ExportActionMixin,ImportExportModelAdmin):
        list_display=('stationName','inspectPH','inspectO2','inspectBOD','inspectSS','inspectCFU','inspectN2','inspectTP','riverStandardPoint','riverStandard')



# Register your models here.
