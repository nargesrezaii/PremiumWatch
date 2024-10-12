from django.db import models
from django.utils import timezone
from datetime import timedelta

from users.models import User


class SubscriptionType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    #Add to ERD
    price = models.IntegerField()
    duration_in_days = models.IntegerField()
    priority_level = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    subscription_type = models.ForeignKey(SubscriptionType, on_delete=models.PROTECT)
    start_time = models.DateTimeField(editable=False)
    end_time = models.DateTimeField(editable=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.subscription_type.name}"

    def is_valid(self):
        return self.is_active and self.end_time > timezone.now()
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.start_time = timezone.now()
            self.end_time = self.start_time + timedelta(days=self.subscription_type.duration_in_days)
        super().save(*args, **kwargs)


