from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(unique=True, max_length=255, null=False)

    def __str__(self):
        return self.name
    
class Album(models.Model):
    name = models.CharField(unique=True, max_length=255, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Track(models.Model):
    name = models.CharField(unique=True, max_length=255, null=False)
    track = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Lyric(models.Model):
    content = models.CharField(unique=True, max_length=255, null=False)
    order =  models.CharField(unique=True, max_length=255, null=False)
    track = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.content