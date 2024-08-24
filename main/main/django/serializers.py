from rest_framework import serializers

from main.django.models import Album, Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ["id", "track_name", "lyrics", "album", "track_order"]


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = [
            "id",
            "album_name",
            "artist_name",
            "album_image_url",
            "genius_url",
            "tracks",
        ]
