from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from videos.models import Video
from videos.models import Category
from videos.serializers import VideoSerializer
from videos.serializers import CategorySerializer


class VideosListCreateAPIView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)


class VideoDetailAPIView(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_field = 'slug'
    

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []