from django.urls import path

from videos.views import VideoUploadView, VideosList, VideoDetailView

urlpatterns = [
    path('', VideosList.as_view(), name='show-videos'),   
    path('upload/', VideoUploadView.as_view(), name='upload'),
    path('<slug:slug>/', VideoDetailView.as_view(), name='video_detail'),
]