from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy

from videos.models import Video
from videos.forms import VideoUploadForm


class VideosList(ListView):
    model = Video
    template_name = 'videos/video_list.html'
    context_object_name = 'videos'
    

class VideoDetailView(DetailView):
    model = Video 
    template_name = 'video_detail.html'
    context_object_name = 'video'
    
    def get_queryset(self):
        return Video.objects.filter(slug=self.kwargs['slug'])
    

class VideoUploadView(CreateView):
    model = Video
    form_class = VideoUploadForm
    template_name = 'videos/upload.html'
    success_url = reverse_lazy('show-videos')
    
    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
    
