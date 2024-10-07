from django.shortcuts import render,HttpResponse
from pytubefix import YouTube
import ffmpeg
# Create your views here.
def home(request):
    if request.method=="POST":
        url=request.POST['url']
        yt=YouTube(url)
        
    return render(request,'home.html')