from django.db import models

class Chargepoint(models.Model):
    name = models.fields.CharField(max_length=100)
    number_of_chargepoint = models.fields.IntegerField()
    puissance_max_w = models.fields.FloatField()

class Customer(models.Model):
    name = models.fields.CharField(max_length=100)
    # chargepoint = ...
    total_payed = models.fields.FloatField()
