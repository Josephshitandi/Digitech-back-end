from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets




class UserSerializer(serializers.ModelSerializer):
    # neighbourhood = serializers.CharField(source='neighbourhood.name')
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','is_staff', 'avatar','password']
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)
    

