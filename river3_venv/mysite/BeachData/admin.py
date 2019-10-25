#RiverStation admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from BeachData.models import BeachDataModel

# Register your models here.
@admin.register(BeachDataModel)
class BeachDataAdmin(ImportExportModelAdmin):
    list_display = ('riverName', 'areaName', 'stationName', 'riverStandard', 'riverstationNumber', 'distanceKM', 'stationAddress', 'stationLocationEast', 'stationLocationNorth', 'stationModeBridge', 'stationModeRiver', 'stationModeRiverside','monitorItem')
    
