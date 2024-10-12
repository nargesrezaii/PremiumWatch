from django.urls import path

from subscription import views

urlpatterns = [
    path('', views.UserSubscriptionView.as_view(), name='user-subscription'),
    path('admin/subscriptions/', views.AdminSubscriptionListView.as_view(), name='admin-subscriptions'),
    path('subscription-types/', views.SubscriptionTypeListView.as_view(), name='subscription-types'),
]
