from django.db import models

# Create your models here.
class BeachDataModel(models.Model):
    NameTest = models.CharField(max_length=10)
