import json

from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.utils.safestring import mark_safe

User = get_user_model()


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {"room_name_json": mark_safe(json.dumps(room_name))})
