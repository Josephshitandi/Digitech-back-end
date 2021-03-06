from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','is_staff', 'avatar','password']
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)
    
class UserRegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    def validate_email(self, email):
        existing = User.objects.filter(email=email).first()
        if existing:
            raise serializers.ValidationError("Someone with that email "
                "address has already registered. Was it you?")
        return email
    
    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("Please enter a password and "
                "confirm it.")
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data

        

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'email', 'status', 'image','user')
        
class SiteSerializer(serializers.ModelSerializer):
    admin = serializers.ReadOnlyField(source ='user.first_name')
    class Meta:
        model = Site
        fields = ('id', 'name', 'email', 'location', 'image','admin','description')
        
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source ='user.first_name')
    site = serializers.ReadOnlyField(source ='site.name')
    class Meta:
        model = Review
        fields = ('id', 'title', 'text', 'date', 'site','user')
        
