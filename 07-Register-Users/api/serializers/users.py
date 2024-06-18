from rest_framework import serializers
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
        