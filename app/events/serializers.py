from rest_framework import serializers

from .models import Event
from performances.serializers import PerformanceSerializer

class EventSerializer(serializers.ModelSerializer):
    performances = PerformanceSerializer(read_only=True, many=True)
    class Meta:
        model = Event
        fields = ('name', 'start', 'end', 'performances')