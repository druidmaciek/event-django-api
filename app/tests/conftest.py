import pytest

from artists.models import Artist
from events.models import Event
from performances.models import Performance

@pytest.fixture(scope="function")
def add_artist():
    def _add_artist(name, genre):
        return Artist.objects.create(name=name, genre=genre)
    return _add_artist

@pytest.fixture(scope="function")
def add_event():
    def _add_event(name, start, end):
        return Event.objects.create(name=name, start=start, end=end)
    return _add_event

@pytest.fixture(scope="function")
def add_performance():
    def _add_performance(artist, event, start, end):
        return Performance.objects.create(artist=artist, event=event, start=start, end=end)
    return _add_performance