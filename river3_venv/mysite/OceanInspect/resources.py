#resources.property

#RiverStation admin.py
from django.contrib import admin

# Register your models here.
from import_export import resources
from .models import OceanInspectModel
from .models import import_export


class OceanInspectResource(resources.ModelResource):
    class Meta:
        model = OceanInspectModel
