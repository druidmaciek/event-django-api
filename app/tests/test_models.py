from datetime import datetime, timedelta
import pytest



@pytest.mark.django_db
def test_artist_model(add_artist):
    artist = add_artist(name="Saint Jhn", genre="rap")
    assert artist.name == "Saint Jhn"
    assert artist.genre == "rap"
    assert str(artist) == artist.name

@pytest.mark.django_db
def test_event_model(add_event):
    start = datetime.now()
    end = datetime.now()+timedelta(days=3)
    event = add_event(name="Festival", start=start, end=end)
    assert event.name == "Festival"
    assert event.start == start
    assert event.end == end
    assert str(event) == event.name

@pytest.mark.django_db
def test_performance_model(add_artist, add_event, add_performance):
    start = datetime.now()
    end = datetime.now()+timedelta(days=3)
    artist = add_artist(name="Saint Jhn", genre="rap")
    event = add_event(name="Festival", start=start, end=end)
    performance = add_performance(artist=artist, event=event, start=start, end=end)
    assert performance.artist == artist
    assert performance.event == event
    assert performance.start == start
    assert performance.end == end
    assert str(performance) == "Saint Jhn on Festival"