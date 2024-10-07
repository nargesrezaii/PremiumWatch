from PIL import Image

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/users', null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    national_id = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'\d{10}',
                message='Invalid national ID.'
            ),
        ],
        unique=True,
    )
    phone_number = models.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                regex=r'09\d{9}$',
                message='Invalid phone number.'
            ),    
        ],
        blank=True,
        null=True,
    )
    email = models.EmailField(unique=True)
    birthdate = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_phone_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.avatar:
            avatar_path = self.avatar.path
            with Image.open(avatar_path) as img:
                width, height = img.size
                if width != height:
                    new_dimension = min(width, height)
                    left = (width - new_dimension) / 2
                    top = (height - new_dimension) / 2
                    right = (width + new_dimension) / 2
                    bottom = (height + new_dimension) / 2
                    img = img.crop((left, top, right, bottom))

                img.save(avatar_path)
    
    def __str__(self):
        return self.username



