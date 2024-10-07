from django.urls import path

from videos.views import VideoUploadView, VideosList

urlpatterns = [
    path('', VideosList.as_view(), name='show-videos'),   
    path('upload/', VideoUploadView.as_view(), name='upload'),
]