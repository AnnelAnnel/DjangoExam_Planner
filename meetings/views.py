from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Meeting
from .forms import MeetingForm
from django.http import HttpResponse


def meetings_list(request):
    meetings = Meeting.objects.all()
    return render(request, 'meetings_list.html', {'meetings': meetings})


def meetings_detail(request, id):
    meeting = get_object_or_404(Meeting, id=id)
    return render(request, 'meetings_detail.html', {'meeting': meeting})


def rooms_list(request):
    rooms = Room.objects.filter(available=True)
    return render(request, 'rooms_list.html', {'rooms': rooms})


def create_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Success')
    else:
        form = MeetingForm()
    return render(request, 'create_meeting.html', {'form': form})
