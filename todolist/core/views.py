from django.contrib.auth import login, logout
from rest_framework import generics, permissions
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


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProfileSerializer
    queryset = models.User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})


class PasswordUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.PasswordUpdateSerializer

    def get_object(self):
        return self.request.user
