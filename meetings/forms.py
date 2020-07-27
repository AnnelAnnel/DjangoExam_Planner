from django.forms import ModelForm
from .models import Meeting


class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'date', 'start_time', 'duration', 'room']

