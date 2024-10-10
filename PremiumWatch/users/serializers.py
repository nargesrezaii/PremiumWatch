from rest_framework import serializers

from django.contrib.auth.hashers import make_password

from users.models import User
from videos.models import Video


class UserSerializer(serializers.ModelSerializer):
    videos = serializers.PrimaryKeyRelatedField(many=True, queryset=Video.objects.all())

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'national_id',
                  'phone_number', 'email', 'birthdate', 'videos']
        

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            validated_data['password'] = make_password(password)
        return super().update(instance, validated_data)
        
   
