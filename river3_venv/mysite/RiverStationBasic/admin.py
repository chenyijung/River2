#RiverStation admin.py
from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import RiverStation


@admin.Register(RiverStation)
class RiverStationAdmin(ImportExportModelAdmin):
    pass

admin.site.register(RiverStation,RiverStationAdmin)
