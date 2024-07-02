from django.db import models

""" House model """
class House(models.Model):

    name = models.CharField(max_length=140)
    price = models.PositiveBigIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)