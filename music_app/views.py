from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Songform
from .models import Song

# Create your views here.
def song_upload_and_list (request):
    songs= Song.objects.all()

    if request.method == "POST":
        form = Songform(request.POST, request.FILES)

        if form.is_valid():
            form.save ()
            messages.success(request, "Song uploaded successfully")
            return redirect('song_upload_and_list')
    else:
        form = Songform()

    return render(request, 'song_upload_and_list.html', {'songs': songs, 'form': form})