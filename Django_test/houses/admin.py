from django.contrib import admin
from .models import House

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    
    """Admin Definition for House"""

    list_display = (
        "name",
        "price_per_night",
        "address",
        "pet_allowed",
    )

    list_filter = [
        "price_per_night",
        "pet_allowed"
    ]
