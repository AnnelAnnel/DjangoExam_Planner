from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=2000)
    floor = models.IntegerField(default=1)
    room_number = models.CharField(max_length=50)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Meeting(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now=False)
    start_time = models.TimeField(auto_now=False)
    duration = models.IntegerField(default=10)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

