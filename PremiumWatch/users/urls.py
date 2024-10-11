from django.urls import path

from users import views


urlpatterns = [
    path('', views.UserAPIView.as_view(), name='user-list'),
    path('<int:pk>', views.UserDetails.as_view(), name='user-detail'),
]