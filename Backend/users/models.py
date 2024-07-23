from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoice(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    first_name = models.CharField(
        max_length=150,
        editable=False
    )

    last_name = models.CharField(
        max_length=150,
        editable=False
    )

    profile_photo = models.ImageField()

    name = models.CharField(
        max_length=150,
        default=""
    )

    is_host = models.BooleanField(
        default=False
    )

    gender = models.CharField(
        max_length=100,
        choices=GenderChoices,
    )

    language = models.CharField(
        max_length=2)