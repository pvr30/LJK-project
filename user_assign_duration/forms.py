from django import forms
from .models import *
import datetime


class UserRoomAssignForm(forms.ModelForm):
    def clean(self):
        try:
            user = self.cleaned_data['user']
            room = self.cleaned_data['room']
            duration = self.cleaned_data['duration']
        except Exception as e:
            room = None
            user = None
            duration = None

        if not user:
            raise forms.ValidationError({'user': 'Please assign atleast one user'})
        elif room is None:
            raise forms.ValidationError({'room': f"Please add room"})
        elif duration is None:
            raise forms.ValidationError({'duration': 'Please assign duration'})

        elif room and duration and user:
            if user.is_admin:
                raise forms.ValidationError({'user': 'can not assign duration to admin user'})

            if UserRoomAssign.objects.filter(room=room, user=user).exists():
                user_room = UserRoomAssign.objects.get(room=room, user=user)
                if user_room.duration != duration:
                    user_room.delete()

            if not user.is_admin:
                room_duration_over = RoomDurationOver.objects.filter(user=user, room=room).exists()
                if room_duration_over:
                    room_dur_obj = RoomDurationOver.objects.get(user=user, room=room)
                    room_dur_obj.delete()

                new_room_duration_over = RoomDurationOver(user=user, room=room, duration=duration, remain_duration=duration, is_time_over=False)
                new_room_duration_over.save()

            room.user.add(user)


