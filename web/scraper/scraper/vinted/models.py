from django.db import models
from simple_history.models import HistoricalRecords


class Brand(models.Model):
    name = models.CharField(max_length=300, unique=True)
    vinted_id = models.IntegerField(null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    items_amount = models.IntegerField(null=False)
    entrances = models.IntegerField(null=True)
    history = HistoricalRecords()