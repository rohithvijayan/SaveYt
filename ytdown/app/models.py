from django.db import models

# Create your models here.
class Video(models.Model):
    title=models.CharField(max_length=200)
    duraion=models.DurationField()
    vid_fle=models.FileField(upload_to='media/videos')
    
    def __str__(self):
        return self.title
        