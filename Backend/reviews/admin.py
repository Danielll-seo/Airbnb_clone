from django.contrib import admin
from .models import Review

class Wordfilter(admin.SimpleListFilter):
    title = "Filter by words!"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awsome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return reviews
        
class Ratingfilter(admin.SimpleListFilter):
    title = "Filter by rating!"

    parameter_name = "rating"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("bad", "Bad"),
        ]
    
    def queryset(self, request, rating):
        selected = self.value()
        if selected == "good":
            return rating.filter(rating__gte=3)
        elif selected == "bad":
            return rating.filter(rating__lt=3)
        else:
            return rating

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
        "room",
        "experience",
    )

    list_filter = (
        Wordfilter,
        Ratingfilter,
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )