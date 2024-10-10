from pytubefix import YouTube,Playlist
import ffmpeg
import os
pl_url=input("enter url:")

#print(yt.streams.filter(only_audio=True))
#vid_stream=yt.streams.get_by_itag(itag=136).download(output_path='/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/vid_stream',filename=f'{yt.title}-video.mp4')
#aud_stream=yt.streams.get_by_itag(itag=140).download(output_path='/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/aud_stream',filename=f'{yt.title}-audio.mp4')
#input_vid=ffmpeg.input(f'/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/vid_stream/{yt.title}-video.mp4')
#input_aud=ffmpeg.input(f'/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/aud_stream/{yt.title}-audio.mp4')
#ffmpeg.concat(input_vid, input_aud, v=1, a=1).output(f'/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/{yt.title}-final.mp4').run()
print(pl_url)
yt_pl=Playlist(pl_url)
for item in yt_pl.videos:
    vid_stream=item.streams.get_by_itag(itag=136).download(output_path='/home/rohithvijayan/Desktop/SaveYt/y_pyt_pltdown/',filename=f'{item.title}-video.mp4')
    aud_stream=item.streams.get_highest_resolution().download(output_path='/home/rohithvijayan/Desktop/SaveYt/y_pyt_pltdown/',filename=f'{item.title}-audio.mp4')
    aud_stream_path=f'/home/rohithvijayan/Desktop/SaveYt/y_pyt_pltdown/{item.title}-video.mp4'
    vid_stream_path=f'/home/rohithvijayan/Desktop/SaveYt/y_pyt_pltdown/{item.title}-audio.mp4'
    input_vid=ffmpeg.input(aud_stream_path)
    input_aud=ffmpeg.input(vid_stream_path)
    ffmpeg.concat(input_vid, input_aud, v=1, a=1).output(f'/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/playlist/{item.title}-final.mp4').run()
    os.remove(aud_stream_path)
    os.remove(vid_stream_path)
   