from django.db import models
from common.models import CommonModel

class Experience(CommonModel):

    """Experience Model Definition"""

    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    name = models.CharField(
        max_length=250, default=""
    )
    host = models.ForeignKey(
        "users.User", 
        on_delete=models.CASCADE
    )
    price = models.PositiveIntegerField(
        default=0,
    )
    address = models.CharField(
        max_length=250,
    )
    start = models.TimeField(
        default="09:00:00",
    )
    end = models.TimeField(
        default="18:00:00",
    )
    description = models.TextField(
        default="",
    )
    perks = models.ManyToManyField(
        "experiences.Perk",
    )

class Perk(CommonModel):

    """ What is included in the experience """

    name = models.CharField(
        max_length=100,
    )
    details = models.CharField(
        max_length=250,
    )
    explanation = models.TextField(
        default="",
    )