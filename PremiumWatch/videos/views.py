from django.shortcuts import render
from django.views.generic import ListView

from videos.models import Video


class VideosList(ListView):
    model = Video
    template_name = 'videos/all_videos.html'
    context_object_name = 'videos'