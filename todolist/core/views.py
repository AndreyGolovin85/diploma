from rest_framework import generics

from todolist.core.models import User
from todolist.core.serializers import RegistrationSerializer


class RegistrationView(generics.CreateAPIView):
    model = User
    serializer_class = RegistrationSerializer

