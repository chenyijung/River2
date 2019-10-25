#resources.property

#RiverStation admin.py
from django.contrib import admin

# Register your models here.
from import_export import resources
from .models import BeachInspectModel
from .models import import_export


class BeachInspectResource(resources.ModelResource):
    class Meta:
        model = BeachInspectModel
