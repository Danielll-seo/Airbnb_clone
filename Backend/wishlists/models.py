from django.db import models
from common.models import CommonModel

class Wishlist(CommonModel):

    "Wishlist model definition"

    name = models.CharField(
        max_length=150,
    )

    rooms = models.ManyToManyField(
        "rooms.room",
        related_name="wishlists",
    )

    experiences = models.ManyToManyField(
        "experiences.Experience",
        related_name="wishlists",
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="wishlists",
    )

    def __str__(self):
        return self.name