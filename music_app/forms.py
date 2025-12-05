from django import forms
from .models import Song

class songform (forms.ModelForm):
    class Meta:
        model = Song
        fields = ['song_title', 'artist', 'album', 'year_of_release', 'audio_file']