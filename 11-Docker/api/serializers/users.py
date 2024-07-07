from typing import Any, Dict
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import update_last_login
from users.models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    
    id = serializers.UUIDField(source = 'public_id', read_only=True)
    class Meta:
        model = User
        
        fields = ['id', "first_name", "last_name", "email", "is_superuser", "date_joined", "updated"]
        

class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only = True, required=True, validators = [validate_password])
    class Meta:
        model = User
        
        fields = ['first_name', "last_name", "email", "password"]
        
        
        
    def create(self, validated_data):
        
        user = User.objects.create_user(**validated_data)
        
        # user = User.objects.create(
        #     first_name=validated_data['first_name'],
        #     last_name=validated_data['last_name'],
        #     email=validated_data['email']
        # )
        return user        
        
        
class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        refresh = self.get_token(user=self.user)
        
        user = UserSerializer(self.user).data
        
        data['refresh'] = str(refresh)
        
        data['access'] = str(refresh.access_token)
        
        data['user'] = user
        
        update_last_login(None, self.user)
        
        return data
    
    
        