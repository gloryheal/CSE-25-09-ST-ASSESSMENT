from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_upload_and_list, name= 'song_upload_and_list'),
]