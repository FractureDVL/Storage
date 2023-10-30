from rest_framework import serializers
from django.contrib.auth.models import User
from apps.user.serializers.user import UserSerializer

class RegisterUserSerializer(UserSerializer):
    email = serializers.EmailField(required=True)
    class Meta:
        model = User
        fields = ['id','information', 'first_name','last_name', 'email', 'is_active', 'password']
    
    def create(self, validated_data):
        instance = super().create(validated_data)
        self.context['user_created'] = instance
        return instance
        