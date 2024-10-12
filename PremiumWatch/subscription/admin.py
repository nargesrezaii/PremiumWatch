from django.contrib import admin

from subscription.models import Subscription
from subscription.models import SubscriptionType

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'subscription_type', 'start_time', 'end_time', 'is_active',)
    search_fields = ('user', 'subscription_type', 'is_active',)

@admin.register(SubscriptionType)
class SubscriptionTypeAdmin(admin.ModelAdmin):
    list_display = ('name','price',)
    search_fields = ('name','price',)
