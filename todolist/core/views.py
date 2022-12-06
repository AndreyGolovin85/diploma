from django.contrib.auth import login
from rest_framework import generics
from rest_framework.response import Response

from . import models
from . import serializers


class RegistrationView(generics.CreateAPIView):
    model = models.User
    serializer_class = serializers.RegistrationSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request=request, user=user)
        return Response(serializer.data)
