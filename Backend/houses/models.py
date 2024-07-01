from django.db import models

class House(models.Model):

    name = models.CharField(max_length=140)
    price = models.PositiveBigIntegerField()
    