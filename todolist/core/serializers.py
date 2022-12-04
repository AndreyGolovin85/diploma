from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from todolist.core.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_repeat = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.get("password")
        password_repeat = validated_data.pop("password_repeat")

        if password != password_repeat:
            raise serializers.ValidationError("Пароли не совпадают")

        hashed_password = make_password(password)
        validated_data["password"] = hashed_password
        instance = super().create(validated_data)
        return instance

    class Meta:
        model = User
        fields = "__all__"
