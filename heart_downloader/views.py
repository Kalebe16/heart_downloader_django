import os
import re

from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from pytube import YouTube

# Create your views here.

# ------- VIEWS -------------------------


def home(request):
    remove_files()

    return render(request, 'pages/home.html')


def download(request):
    """ pegando dados do formulario """
    global link, video, titulo_video
    link = request.POST.get('link')

    # verificando se é um link valido
    try:
        video = YouTube(link)
        titulo_video = video.title
        thumbnail_video = video.thumbnail_url

        return render(request, 'pages/download.html', {"link": link, "titulo_video": titulo_video, "thumbnail_video": thumbnail_video})

    except:
        return HttpResponse("LINK INVÁLIDO")


def mp4(request):

    if request.method == 'GET':
        video.streams.get_highest_resolution().download()

        return FileResponse(open(YouTube(link).streams.get_highest_resolution().download(), 'rb'), as_attachment=True)


def mp3(request):
    remove_files()

    if request.method == 'GET':

        filename = video.title
        filename.replace(",", "")

        file_mp4 = video.streams.get_audio_only().download(filename=filename)
        base, ext = os.path.splitext(file_mp4)
        my_mp3 = base + '.mp3'
        os.rename(file_mp4, my_mp3)
        name_file = filename + ".mp3"
        return FileResponse(open(name_file, 'rb'), as_attachment=True)


# ------- FUNÇÕES AUXILIARES -------------------------
def remove_files():
    """ Exclui os arquivos mp3, mp4 do servidor """
    # For para percorrer dentro da pasta passada anteriormente
    for file in os.listdir('.'):
        if re.search('mp4', file):  # If verificando se o arquivo e .MP4
            mp4_path = os.path.join('.', file)
            os.remove(mp4_path)
        elif re.search('mp3', file):  # If verificando se o arquivo e .MP4 3
            mp3_path = os.path.join('.', file)
            os.remove(mp3_path)
