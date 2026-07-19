from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room

class RoomDetailSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price"
        )

class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"