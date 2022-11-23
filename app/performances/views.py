from rest_framework import generics
from django.shortcuts import get_object_or_404 

from .models import Performance
from .serializers import PerformanceSerializer
from events.models import Event


class PerformanceMixin:
    serializer_class = PerformanceSerializer

    def get_queryset(self):
        event_id = self.kwargs.get('event_id')
        event = get_object_or_404(Event, pk=event_id)
        return Performance.objects.filter(event=event)

class PerformanceList(PerformanceMixin, generics.ListCreateAPIView):
    pass
    

class PerformanceDetail(PerformanceMixin, generics.RetrieveUpdateDestroyAPIView):
    pass
