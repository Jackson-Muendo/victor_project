from django.shortcuts import render
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    from django.shortcuts import render, redirect
    from .forms import EventForm

def events_list(request):
    events = Event.objects.all()
    return render(request, 'events/events_list.html', {'events': events})


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events_list')  # Redirect to a page displaying the list of events
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})
