from rest_framework import generics

from . import models
from . import serializers


class RegistrationView(generics.CreateAPIView):
    model = models.User
    serializer_class = serializers.RegistrationSerializer

