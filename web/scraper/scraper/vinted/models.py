from django.db import models
from simple_history.models import HistoricalRecords


class Brand(models.Model):
    name = models.CharField(max_length=300, unique=True, null=False)
    vinted_id = models.IntegerField(null=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    items_amount = models.IntegerField(null=True)
    entrances = models.IntegerField(null=True)
    history = HistoricalRecords()

    class Meta:
        app_label = 'scraper.vinted'


class Item(models.Model):
    vinted_id = models.IntegerField(null=False, unique=True)
    brand = models.ForeignKey(to=Brand,on_delete=models.CASCADE),
    currency = models.CharField(max_length=10)
    user_price = models.FloatField(null=False)
    service_fee = models.FloatField(null=False)
    total_price = models.FloatField(null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        app_label = 'scraper.vinted'
