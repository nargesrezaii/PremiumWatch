from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import PermissionDenied

from subscription.models import Subscription
from subscription.models import  SubscriptionType
from subscription.serializers import SubscriptionSerializer
from subscription.serializers import SubscriptionTypeSerializer
from users.models import User


class UserSubscriptionView(generics.RetrieveUpdateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        subscription = Subscription.objects.filter(user=self.request.user).first()
        if not subscription:
            raise PermissionDenied("You do not have an active subscription.")
        return subscription


class AdminSubscriptionListView(generics.ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAdminUser]


class SubscriptionTypeListView(generics.ListAPIView):
    queryset = SubscriptionType.objects.all()
    serializer_class = SubscriptionTypeSerializer
    permission_classes = [permissions.AllowAny]
