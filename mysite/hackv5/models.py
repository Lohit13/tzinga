from django.db import models
from django import forms
import csv
# Create your models here.

class Byld(models.Model):
    field1 = models.CharField(max_length=200)
    field2 = models.CharField(max_length=200)
    field3 = models.CharField(max_length=200)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.field1


class Byldmess(models.Model):
    field11 = models.CharField(max_length=200)
    field21 = models.CharField(max_length=200)
    field31 = models.CharField(max_length=200)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.field11


