#RiverStation admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin,ExportActionMixin

from OceanData.models import OceanDataModel

# Register your models here.
@admin.register(OceanDataModel)
class OceanDataAdmin(ExportActionMixin,ImportExportModelAdmin):
    list_display = ('riverName', 'areaName', 'stationName', 'riverStandard', 'riverstationNumber', 'distanceKM', 'stationAddress', 'stationLocationEast', 'stationLocationNorth', 'stationModeBridge', 'stationModeRiver', 'stationModeRiverside','monitorItem')
