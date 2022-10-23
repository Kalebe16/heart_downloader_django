from django.urls import path

from heart_downloader.views import download, home, mp3, mp4

urlpatterns = [
    path('', home),  # HOME
    path('download', download, name='download'),
    path('mp4', mp4, name='mp4'),
    path('mp3', mp3, name='mp3')



]
