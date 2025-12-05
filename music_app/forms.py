from django import forms
from .models import Song

class Songform (forms.ModelForm):
    class Meta:
        model = Song
        fields = ['song_title', 'artist', 'album', 'year_of_release', 'audio_file']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'song_title': 'Song title',
            'artist': 'Artist',
            'album': 'Album',
            'year_of_release': 'Year of release',
            'audio_file': 'Upload audio file',}
        
        #Bootstrap classes and placeholders to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
            })

            if field_name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[field_name]
