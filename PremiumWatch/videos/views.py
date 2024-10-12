from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from videos.models import Video
from videos.models import Category
from users.models import User
from subscription.models import Subscription
from videos.serializers import VideoSerializer
from videos.serializers import CategorySerializer


class VideosListCreateAPIView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        for video_data in response.data:
            video_data.pop('file', None)

        return Response(response.data)

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)


class VideoDetailAPIView(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]
    
    def get(self, request, *args, **kwargs):
        video = self.get_object()

        if request.user.is_authenticated and request.user.is_admin:
            return super().get(request, *args, **kwargs)
        
        if request.user.is_authenticated and request.user == video.uploaded_by:
            return super().get(request, *args, **kwargs)

        if not request.user.is_authenticated:
            response_data = self.get_serializer(video).data
            response_data.pop('file')  
            return Response(response_data)
        
        if not self.user_has_access_to_video(request.user, video):
            raise PermissionDenied("You need a subscription to view this video file.")

        return super().get(request, *args, **kwargs)
    
    def user_has_access_to_video(self, user, video):
        user_subscription = Subscription.objects.filter(user=user, is_active=True).first()
        if user_subscription and user_subscription.subscription_type.priority_level >= video.required_subscription_type.priority_level:
            return True
        return False
    

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]