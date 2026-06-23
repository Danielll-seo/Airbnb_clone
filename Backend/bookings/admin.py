from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class Booking(admin.ModelAdmin):
    pass
