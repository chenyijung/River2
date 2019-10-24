#resources.property

#RiverStation admin.py
from django.contrib import admin

# Register your models here.
from import_export import resources
from .models import OceanDataModel
from .models import import_export


class OceanDataResource(resources.ModelResource):

    class Meta:
        model = OceanDataModel
