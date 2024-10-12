from rest_framework import serializers

from videos.models import Video 
from videos.models import Category
from subscription.models import Subscription


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'id', 'title', 'category', 'description', 'thumbnail', 'file',
            'created_at', 'uploaded_by', 'views', 'required_subscription'
        ]
        

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'