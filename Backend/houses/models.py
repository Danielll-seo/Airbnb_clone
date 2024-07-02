from django.db import models

""" Model definition for Houses """
class House(models.Model):

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveBigIntegerField(verbose_name="Price", help_text="positive number only")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        verbose_name="Pets allowed?",
        default=True,
        help_text="Does this house allows pets?"
    )

    def __str__(self):
        return self.name