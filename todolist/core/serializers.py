from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.validators import UniqueValidator

from . import models


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_repeat = serializers.CharField(write_only=True)

    def validate(self, attrs):
        password = attrs.get("password")
        password_repeat = attrs.pop("password_repeat")

        if password != password_repeat:
            raise serializers.ValidationError("Пароли не совпадают")

        try:
            validate_password(password)
        except Exception as error:
            raise serializers.ValidationError({"password": error.messages})

        return attrs

    def create(self, validated_data):
        password = validated_data.get("password")

        hashed_password = make_password(password)
        validated_data["password"] = hashed_password
        instance = super().create(validated_data)
        return instance

    class Meta:
        model = models.User
        fields = "__all__"


class RetrieveUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        validators=[
            UniqueValidator(queryset=models.User.objects.all())
        ]
    )

    class Meta:
        model = models.User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email'
        )


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def create(self, validated_data):
        user = authenticate(
            username=validated_data["username"],
            password=validated_data["password"],
        )

        if not user:
            raise AuthenticationFailed
        return user

    class Meta:
        model = models.User
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ("id", "username", "first_name", "last_name", "email")


class PasswordUpdateSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        user = attrs["user"]

        if not user.check_password(attrs["old_password"]):
            raise serializers.ValidationError({"old_password": "Пароль неверный"})
        try:
            validate_password(attrs["new_password"])
        except Exception as error:
            raise serializers.ValidationError({"new_password": error.messages})
        return attrs

    def update(self, instance, validated_data):
        instance.password = make_password(validated_data["new_password"])
        instance.save()
        return instance
