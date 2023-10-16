from rest_framework import serializers
from.models import Beach
from.models import Video


class BeachSerializer(serializers.ModelSerializer):
  class Meta:
    model = Beach
    fields = ['id','name','description' , 'image_url']
    

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'video_file']