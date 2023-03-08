from apps.user.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.get('password')
        user = User(
            username=validated_data.get('username'),
            password=password,
            name=validated_data.get('name'),
        )
        user.set_password(password)
        user.save()

        return user
    
    def validate(self, data):
        id = data.get('id', None)

        if User.objects.filter(id=id).exists():
            raise serializers.ValidationError("Username already exists")

        data['date_joined'] = date.today()

        return data