from django.db import models

class House(models.Model):

    """Model Definition for Houses"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(
        verbose_name="Price",
        help_text="Price per night in KRW"
    )
    description = models.TextField()
    address = models.CharField(max_length=140)
    pet_allowed = models.BooleanField(
        verbose_name="Pet Allowed?",
        default=True,
        help_text="Is pet allowed in this house?"
    )

    def __str__(self):
        return self.name