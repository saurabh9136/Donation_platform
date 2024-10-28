from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import User, NGO, Donation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'first_name','last_name', 'email', 'mobile_number', 'password', 'address', 'country_region','city', 'status', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

class NGOSerializer(serializers.ModelSerializer):
    class Meta:
        model = NGO
        fields = '__all__'
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(NGOSerializer, self).create(validated_data)

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'
        read_only_fields = ['donation_id', 'donation_date']
    
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Donation amount must be positive.")
        return value

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        user = authenticate(request=None, email=email, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid email or password")
        return {'user': user}
    
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
