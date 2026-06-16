from django.db import models

"""
this file is for the common model that will be used in other apps.
so we can avoid code duplication and keep our code DRY
(Don't Repeat Yourself) principle.
"""
class CommonModel(models.Model):

    """Common Model Definition"""

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True 