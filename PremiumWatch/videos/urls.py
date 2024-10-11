from django.urls import path

from videos import views

urlpatterns = [
    path('', views.VideosListCreateAPIView.as_view(), name='videos-list-create'),   
    path('<slug:slug>', views.VideoDetailAPIView.as_view(), name='video-detail'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
]