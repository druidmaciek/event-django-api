from collections import namedtuple

from rest_framework import serializers

from .models import Performance


Range = namedtuple('Range', ['start', 'end'])

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ("id", 'artist', 'start', 'end', 'event')

    def validate(self, data):
        """
        Check dates overlap etc.
        """
        event = data['event']
        print(event.start, event.end)
        print(event.performances.values_list('start', 'end'))
        if data['start'] > data['end']:
            raise serializers.ValidationError({"end": "finish must occur after start"})
        # check if start end is in the range of start/end of event
        if data['start'] < event.start or data['end'] > event.end:
            raise serializers.ValidationError({"end": "Performance is outside of event dates"})
        # check if it overlaps with other events
        new_performance_range = Range(start=data['start'], end=data['end'])
        for start, end in event.performances.values_list('start', 'end'):
            performance_range = Range(start=start, end=end)
            latest_start = max(new_performance_range.start, performance_range.start)
            earliest_end = min(new_performance_range.end, performance_range.end)
            delta = (earliest_end - latest_start).total_seconds() + 1
            overlap = max(0, delta)
            print(overlap, 'overlap')
            if overlap > 0:
                raise serializers.ValidationError({"start": "There is an overlap with another event"})
        return data