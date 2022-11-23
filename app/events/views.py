import csv

import requests
from django.http import JsonResponse
from django_q.tasks import async_task
from rest_framework import generics

from .models import Event
from .serializers import EventExportSerializer, EventSerializer


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


def export_csv(webhook):

    data = [
        {"name": x.name, "start": str(x.start), "end": str(x.end)}
        for x in Event.objects.all()
    ]
    keys = data[0].keys()

    with open("events.csv", "w", newline="") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

    requests.post(
        webhook, data={"msg": "Export complete", "csv_url": "/media/events.csv"}
    )


class ExportCSVEvents(generics.CreateAPIView):
    serializer_class = EventExportSerializer

    def post(self, request, *args, **kwargs):
        serializer = EventExportSerializer(data=request.data)
        if serializer.is_valid():
            async_task("events.export_csv", serializer.data["webhook"])
            return JsonResponse({"message": "export task started"})
        return JsonResponse({"message": "webhook not valid"})
