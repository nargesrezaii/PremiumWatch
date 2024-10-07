from django.urls import path

from videos.views import VideosList

urlpatterns = [
    path('show-all/', VideosList.as_view(), name='videos'),    
]