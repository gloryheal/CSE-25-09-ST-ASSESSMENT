from django.shortcuts import render, redirect
from django.contrib.auth import messages
from .forms import songform
from .models import Song

# Create your views here.
def song_upload_and_list (request):
    songs= Song.objects.all()

    if request.method == "POST":
        form=songform(request.POST)

        if form.is_valid():
            form.save
            message.success(request, "Song uploaded successfully")
            return redirect('song_upload_and_list')
    else:
        song = songform()

    return render(request, 'music_app/song_upload_and_list.html')

