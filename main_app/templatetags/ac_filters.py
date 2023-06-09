from django import template
from ..models import AC, Room
from user_assign_duration.models import *

register = template.Library()

@register.filter
def rooms_ac(room, user):
    if user.is_admin:
        room = Room.objects.get(room_id=room.room_id)
        return AC.objects.filter(room=room).order_by('created_at')
    else:
        room = Room.objects.get(room_id=room.room_id, user=user)
        return AC.objects.filter(room=room).order_by('created_at')

@register.filter
def room_color(room, user):
    try:
        room_assign_over_exists = RoomDurationOver.objects.filter(user=user, room=room).exists()
        if room_assign_over_exists:
            room_assign_over = RoomDurationOver.objects.get(user=user, room=room)
            status = room_assign_over.is_time_over
            return status
    except Exception as e:
        print(e)