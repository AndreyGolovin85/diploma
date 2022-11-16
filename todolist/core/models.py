from django.contrib.auth.models import AbstractUser
from django.db import models


class AbstractUser(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveSmallIntegerField(default=0)
