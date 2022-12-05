from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from . import models


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_repeat = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.get("password")
        password_repeat = validated_data.pop("password_repeat")

        if password != password_repeat:
            raise serializers.ValidationError("Пароли не совпадают")

        try:
            validate_password(password)
        except Exception as error:
            raise serializers.ValidationError(error.args[0])

        hashed_password = make_password(password)
        validated_data["password"] = hashed_password
        instance = super().create(validated_data)
        return instance

    class Meta:
        model = models.User
        fields = "__all__"
