from rest_framework import serializers

from videos.models import Video
        

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'title', 'category', 'description', 'thumbnail'] 