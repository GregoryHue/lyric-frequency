from rest_framework import serializers

from main.django.models import Album, Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ["track_name", "lyrics", "album"]


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ["album_name", "artist_name", "tracks"]
