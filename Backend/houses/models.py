from django.db import models

class House(models.Model):

    """Model Definition for Houses"""

    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    
    # 아몰랑 너무 졸려서 자러갈래 난 간다 ㅃㅇ