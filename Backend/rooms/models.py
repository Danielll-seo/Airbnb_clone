from django.db import models

# Create your models here.
class Room(models.Model):

    """Room Model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField(
        default=False
    ) # cause i don't like pets
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

class Amenity(models.Model):

    """Amenity Model Definition"""

    name = models.CharField(
        max_length=150,
    )
    description = models.CharField(
        max_length=150,
        default="",
    )

"""
"Many to Many" 관계는 "다대다" 관계라고 불립니다. 하나의 방은 여러 개의 편의 시설을 가질 수 있고,
하나의 편의 시설은 여러 개의 방에서 사용될 수 있기 때문에, 이 두 테이블을 연결하는 새로운 테이블이 필요합니다.
그렇다면 Many to one 이나 One to one, One to Many 은 무엇인가?
One to Many 관계는 하나의 방이 여러 개의 호스트를 가질 수 있지만, 하나의 호스트는 하나의 방을 가질 수 있는 관계입니다.
Many to one 관계는 하나의 방이 하나의 호스트를 가질 수 있지만, 하나의 호스트는 여러 개의 방을 가질 수 있는 관계입니다.
One to one 관계는 하나의 방이 하나의 호스트를 가질 수 있고, 하나의 호스트도 하나의 방을 가질 수 있는 관계입니다.
"""