from django.db import models

# Create your models here.
class Song (models.Model):
    song_title =models.CharField(max_length=250)
    artist = models.CharField( max_length=250)
    album = models.CharField(max_length= 250)
    year_of_release = models.IntegerField
    audio_file = models.FileField

    def __str__(self):
        return f"{self.song_title},\n{self.artist}, {self.album}"
