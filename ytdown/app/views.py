from django.shortcuts import render,HttpResponse
from django.http import FileResponse
from pytubefix import YouTube,Playlist
import ffmpeg
from app.models import *
from django.core.files import File
import os
# Create your views here.
def home(request):
    if request.method=="POST":
        url=request.POST['link']
        yt=YouTube(url)
        if 'video' in request.POST:
            
            vid_stream=yt.streams.get_by_itag(itag=136).download(output_path='/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/vid_stream',filename=f'{yt.title}-video.mp4')
            aud_stream=yt.streams.get_by_itag(itag=140).download(output_path='/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/aud_stream',filename=f'{yt.title}-audio.mp4')
            aud_stream_path=f'/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/vid_stream/{yt.title}-video.mp4'
            vid_stream_path=f'/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/aud_stream/{yt.title}-audio.mp4'
            input_vid=ffmpeg.input(aud_stream_path)
            input_aud=ffmpeg.input(vid_stream_path)
            ffmpeg.concat(input_vid, input_aud, v=1, a=1).output(f'/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/{yt.title}-final.mp4').run()
            video=Video()
            video.title=yt.title
            video.duraion=yt.length/60
            final_vid_file_path=f'/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/{yt.title}-final.mp4'
            with open(final_vid_file_path,'rb') as finalVideo:
                video.vid_fle.save(name=f"{yt.title}-download.mp4",content=File(finalVideo))
            os.remove(aud_stream_path) 
            os.remove(vid_stream_path) 
            os.remove(final_vid_file_path)
            video.save()
            return FileResponse(video.vid_fle,as_attachment=True)
    if 'audio' in request.POST:
        audio=yt.streams.get_audio_only().download(output_path=f'/home/rohithvijayan/Desktop/SaveYt/ytdown/media/audio',filename=f'{yt.title}-audio.mp4')
        song=Video()
        song.title=yt.title
        song.duraion=yt.length/60
        song_file_path=f'/home/rohithvijayan/Desktop/SaveYt/ytdown/media/audio/{yt.title}-audio.mp4'
        with open(file=song_file_path,mode='rb') as aud:
            song.audio_file.save(name=f"{yt.title}-download.mp4",content=File(aud))
        song.save()
        return FileResponse(song.audio_file,as_attachment=True)
    return render(request,'home.html')
#----------------------------------------------------------------PLAYLIST DOWNLOADS----------------------------------------------------------------
def playlist_download(request):
    if request.method=="POST":
        pl_url=request.POST['playlist_link']
        print(pl_url)
        yt_pl=Playlist(pl_url)
        for item in yt_pl.videos:
            vid_stream=item.streams.get_by_itag(itag=136).download(output_path='/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/vid_stream',filename=f'{item.title}-video.mp4')
            aud_stream=item.streams.get_by_itag(itag=140).download(output_path='/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/aud_stream',filename=f'{item.title}-audio.mp4')
            aud_stream_path=f'/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/vid_stream/{item.title}-video.mp4'
            vid_stream_path=f'/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/aud_stream/{item.title}-audio.mp4'
            input_vid=ffmpeg.input(aud_stream_path)
            input_aud=ffmpeg.input(vid_stream_path)
            ffmpeg.concat(input_vid, input_aud, v=1, a=1).output(f'/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/playlist/{item.title}-final.mp4').run()
            video=Video()
            video.title=item.title
            video.duraion=item.length/60
            final_vid_file_path=f'/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/playlist/{item.title}-final.mp4'
            with open(final_vid_file_path,'rb') as finalVideo:
                video.vid_fle.save(name=f"{item.title}-download.mp4",content=File(finalVideo))
            os.remove(aud_stream_path) 
            os.remove(vid_stream_path) 
            video.save()
        return FileResponse(video.vid_fle,as_attachment=True)               
    return render(request,'playlist.html')
    
