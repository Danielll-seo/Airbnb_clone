from django.shortcuts import render
from django.http import HttpResponse

def see_all_rooms(request):
    return HttpResponse("see all rooms!")

def see_one_room(request):
    return HttpResponse("see a room")