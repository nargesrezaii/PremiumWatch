from email.policy import default
from django.db import models
from django.db.models.fields import related
from django.utils.text import slugify

from users.models import User
from subscription.models import SubscriptionType


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # add these fields to ERD
    file = models.FileField(upload_to='videos/', blank=False, null=False)
    views = models.PositiveIntegerField(default=0)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='videos')
    slug = models.SlugField(unique=True, blank=True)
    required_subscription = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE, default=1)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            original_slug = self.slug
            counter = 1
            while Video.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title