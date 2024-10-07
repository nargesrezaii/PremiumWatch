from django import forms

from videos.models import Video

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'category', 'description', 'thumbnail', 'file']