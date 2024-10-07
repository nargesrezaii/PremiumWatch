from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'first_name', 'last_name',  'email', 'is_active', 
        'is_admin', 'is_email_verified', 'is_phone_verified'
    )
    search_fields = ('username', 'email', 'first_name', 'last_name', 'national_id')

