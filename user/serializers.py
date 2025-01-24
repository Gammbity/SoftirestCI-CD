from rest_framework import serializers
from user.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError 

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'phone', 'password']
    
    def validate_password(validated_data, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise ({"error": e})
        return value
    
    def validate_phone(validated_data, value):
        if len(value) != 13:
            raise serializers.ValidationError("Phone number must be 13 characters")
        return value
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)