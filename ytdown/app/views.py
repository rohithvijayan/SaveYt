from django.shortcuts import render,HttpResponse
from django.http import FileResponse
from pytubefix import YouTube
import ffmpeg
from app.models import *
from django.core.files import File
import os
# Create your views here.
def home(request):
    if request.method=="POST":
        url=request.POST['link']
        yt=YouTube(url)
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
    return render(request,'home.html')

    
