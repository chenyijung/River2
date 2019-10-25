#RiverStation admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from RiverStationBasic.models import RiverStation


# Register your models here.
@admin.register(RiverStation)

class RiverStationAdmin(ImportExportModelAdmin):
    list_display = ('riverName', 'areaName', 'stationName', 'riverStandard', 'riverstationNumber', 'distanceKM', 'stationAddress', 'stationLocationEast', 'stationLocationNorth', 'stationModeBridge', 'stationModeRiver', 'stationModeRiverside','monitorItem')


#admin.site.register(RiverStation)
#admin.site.register(ImportExportMixin)
