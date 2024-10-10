from pytubefix import YouTube
import ffmpeg
url=input("enter url:")
yt=YouTube(url)
print (yt.streams.filter(only_audio=True))
audio=yt.streams.get_audio_only().download()
#print(yt.streams.filter(only_audio=True))
#vid_stream=yt.streams.get_by_itag(itag=136).download(output_path='/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/vid_stream',filename=f'{yt.title}-video.mp4')
#aud_stream=yt.streams.get_by_itag(itag=140).download(output_path='/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/aud_stream',filename=f'{yt.title}-audio.mp4')
#input_vid=ffmpeg.input(f'/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/vid_stream/{yt.title}-video.mp4')
#input_aud=ffmpeg.input(f'/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/aud_stream/{yt.title}-audio.mp4')
#ffmpeg.concat(input_vid, input_aud, v=1, a=1).output(f'/home/rohithvijayan/Desktop/SaveYt/ytdown/media/videos/{yt.title}-final.mp4').run()