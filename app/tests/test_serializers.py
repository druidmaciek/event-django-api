import pytest

from artists.serializers import ArtistSerializer
from events.serializers import EventSerializer
from performances.serializers import PerformanceSerializer


@pytest.mark.django_db
def test_valid_artist_serializer():
    valid_artist_serializer = {
        "name": "Saint Jhn",
        "genre": "rap"
    }
    serializer = ArtistSerializer(data=valid_artist_serializer)
    assert serializer.is_valid()
    assert serializer.validated_data["name"] == valid_artist_serializer["name"]
    assert serializer.validated_data["genre"] == valid_artist_serializer["genre"]
    assert serializer.data == valid_artist_serializer
    assert serializer.errors == {}


@pytest.mark.django_db
def test_invalid_artist_serializer():
    invalid_serializer_data = {
        "name": "Saint Jhn",
    }
    serializer = ArtistSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"genre": ["This field is required."]}
