from django.contrib import admin

# Register your models here.
from import_export import resources
from .models import RiverStation

class RiverResourceAdmin(resources.ModelResource):
    list_display = ("riverName", "areaName", "stationName", "riverStandard", "riverstationNumber", "distanceKM", "stationAddress", "stationLocationEast", "stationLocationNorth", "stationModeBridge", "stationModeRiver", "stationModeRiverside","monitorItem")
    class Meta:
        model = RiverStation
admin.site.register(RiverStation, RiverResourceAdmin)
