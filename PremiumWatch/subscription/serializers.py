from rest_framework import serializers
from django.utils import timezone
from datetime import timedelta

from subscription.models import Subscription
from subscription.models import SubscriptionType


class SubscriptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionType
        fields = ['id', 'name', 'price', 'duration_in_days']
        

class SubscriptionSerializer(serializers.ModelSerializer):
    subscription_type = SubscriptionTypeSerializer(read_only=True)
    subscription_type_id = serializers.PrimaryKeyRelatedField(
        queryset=SubscriptionType.objects.all(), 
        write_only=True, 
        source='subscription_type'
        )

    class Meta:
        model = Subscription
        fields = ['id', 'subscription_type', 'subscription_type_id', 'start_time', 'end_time', 'is_active']

    def update(self, instance, validated_data):
        if 'subscription_type' in validated_data:
            new_subscription_type = validated_data.pop('subscription_type')
            instance.subscription_type = new_subscription_type
            instance.start_time = timezone.now()
            instance.end_time = instance.start_time + timedelta(days=new_subscription_type.duration_in_days)
        return super().update(instance, validated_data)