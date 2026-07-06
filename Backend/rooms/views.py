from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
from categories.models import Category


def see_all_rooms(request):
    rooms = Room.objects.all()
    categories = Category.objects.all()

    selected_category_pk = request.GET.get("category")
    if selected_category_pk:
        rooms = rooms.filter(category_id=selected_category_pk)

    selected_category = None
    if selected_category_pk:
        selected_category = categories.filter(pk=selected_category_pk).first()

    return render(
        request,
        "all_rooms.html",
        {
            "rooms": rooms,
            "categories": categories,
            "selected_category": selected_category,
            "title": "Hello! this title comes from django!"
        },
    )

def see_one_room(request, room_pk):
    try:
        room = Room.objects.get(pk=room_pk)
        return render(
            request,
            "room_detail.html",
            {
                "room": room,
            },
        )
    except Room.DoesNotExist:
        return render(
            request,
            "room_detail.html",
            {
                "not_found": True,
                "room_pk": room_pk
            },
        )