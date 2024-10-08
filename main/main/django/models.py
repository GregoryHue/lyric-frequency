from django.db import models

# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=255, null=False)
    artist_name = models.CharField(max_length=255, null=False)
    album_image_url = models.CharField(max_length=255, null=False)
    genius_url = models.CharField(max_length=255, null=False)

    class Meta:
        unique_together = (
            "album_name",
            "artist_name",
        )

    def __str__(self):
        return self.artist_name + " - " + self.album_name


class Track(models.Model):
    track_name = models.CharField(max_length=255, null=False)
    lyrics = models.TextField(null=False)
    album = models.ForeignKey(Album, related_name="tracks", on_delete=models.CASCADE)
    track_order = models.IntegerField(null=False)

    class Meta:
        ordering = ["track_order"]
        unique_together = (
            "track_name",
            "album",
        )
