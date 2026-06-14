# 이론에 대해서 설명하는 문서고요.
from django.db import models

# MTM, MTO, OTO, OTM 기본 개념
# Many to Many: 하나의 방이 여러 개의 편의 시설을 가질 수 있고, 하나의 편의 시설은 여러 개의 방에서 사용될 수 있는 관계입니다.
# Many to one: 하나의 방이 하나의 호스트를 가질 수 있지만, 하나의 호스트는 여러 개의 방을 가질 수 있는 관계입니다.
# One to one: 하나의 방이 하나의 호스트를 가질 수 있고, 하나의 호스트도 하나의 방을 가질 수 있는 관계입니다.
# One to Many: 하나의 방이 여러 개의 호스트를 가질 수 있지만, 하나의 호스트는 하나의 방을 가질 수 있는 관계입니다.

# Airbnb의 구조를 예로 들어보죠
# 방(Room) 모델과 편의 시설(Amenity) 모델이 있다고 가정해봅시다. 하나의 방은 여러 개의 편의 시설을 가질 수 있고,
# 하나의 편의 시설은 여러 개의 방에서 사용될 수 있기 때문에, 이 두 테이블을 연결하는 새로운 테이블이 필요합니다.
# 이 새로운 테이블은 "Many to Many" 관계를 나타냅니다.
# 또한, 하나의 방은 하나의 호스트를 가질 수 있지만, 하나의 호스트는 여러 개의 방을 가질 수 있기 때문에,
# 방과 호스트 사이에는 "Many to one" 관계가 존재합니다. 만약 하나의 방이 하나의 호스트를 가질 수 있고,
# 하나의 호스트도 하나의 방을 가질 수 있다면, 이는 "One to one" 관계가 됩니다. 반대로,
# 하나의 방이 여러 개의 호스트를 가질 수 있지만, 하나의 호스트는 하나의 방을 가질 수 있다면, 이는 "One to Many" 관계가 됩니다.

# 이걸 대충 코드로 짜보면 다음과 같습니다.
class Room(models.Model):
    # ... other fields ...
    amenities = models.ManyToManyField("Amenity", related_name="rooms")
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms",
    )

class Amenity(models.Model):
    # ... other fields ...
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, default="")

class Host(models.Model):
    # ... other fields ...
    name = models.CharField(max_length=150)
    # ... other fields ... 

# 위 코드에서 Room 모델은 Amenity 모델과 Many to Many 관계를 가지고 있습니다. 하나의 방은 여러 개의 편의 시설을 가질 수 있고,
# 하나의 편의 시설은 여러 개의 방에서 사용될 수 있기 때문에, ManyToManyField를 사용하여 이 관계를 나타냅니다.
# 또한, Room 모델은 Host 모델과 Many to one 관계를 가지고 있습니다. 하나의 방은 하나의 호스트를 가질 수 있지만, 하나의 호스트는 여러 개의
# 방을 가질 수 있기 때문에, ForeignKey를 사용하여 이 관계를 나타냅니다. 만약 Room 모델과 Host 모델이 One to one 관계라면,
# OneToOneField를 사용하여 이 관계를 나타낼 수 있습니다. One to Many
# 관계는 Many to one 관계의 반대이므로, ForeignKey를 사용하여 이 관계를 나타낼 수 있습니다.