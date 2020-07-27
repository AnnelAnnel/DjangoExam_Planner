from django.contrib import admin
from .models import Room, Meeting

# Room - name, floor, room_number
# - Meeting - title,date,start_time,duration,room - (models)


class RoomAdmin(admin.ModelAdmin):
    fields = ['name', 'floor', 'room_number', 'available']
    list_display = ['name', 'floor', 'room_number', 'available']


class MeetingAdmin(admin.ModelAdmin):
    fields = ['title', 'date', 'start_time', 'duration', 'room']
    list_display = ['title', 'date', 'start_time', 'duration', 'room']


admin.site.register(Room, RoomAdmin)

admin.site.register(Meeting, MeetingAdmin)

