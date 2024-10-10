from django.urls import path

from users import views


urlpatterns = [
    path('', views.UserAPIView.as_view(), name='user-list'),
    path('<int:pk>', views.UserDetails.as_view(), name='user-detail'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
]