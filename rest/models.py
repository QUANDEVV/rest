from django.db import models

class Beach(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=500)
  image_url = models.URLField(null=True, blank=True)
  
  
class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
  
  
  
