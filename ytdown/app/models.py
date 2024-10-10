from django.db import models

# Create your models here.
class Video(models.Model):
    title=models.CharField(max_length=200)
    duraion=models.IntegerField()
    vid_fle=models.FileField(upload_to='media/videos',blank=True)
    audio_file=models.FileField(upload_to='media/audio',blank=True)
    def __str__(self):
        return self.title
        