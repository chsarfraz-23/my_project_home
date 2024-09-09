from django.db import models

# Create your models here.

class KollaTesting(models.Model):
    kolla_name = models.CharField(max_length=200, null=True, blank=True)
    kolla_id = models.CharField(max_length=300, null=True, blank=True)
    kolla_connector_name = models.CharField(max_length=300, null=True, blank=True)
