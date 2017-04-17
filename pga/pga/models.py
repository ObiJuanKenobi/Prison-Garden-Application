from __future__ import unicode_literals

from django.db import models
from django import forms
from django.core.urlresolvers import reverse


class GardenImages(models.Model):
    PlanID = models.IntegerField(primary_key=True)
    Bed_Name = models.CharField(max_length=45)
    Bed_Canvas = models.TextField
    Updated_At = models.DateTimeField(auto_now=True, auto_now_add=False)
    Created_At = models.DateTimeField(auto_now=False, auto_now_add=True)
    class Meta:
        managed = False
        db_table = 'Bed_Plans'

class DataFile(models.Model):
    data = models.FileField()
