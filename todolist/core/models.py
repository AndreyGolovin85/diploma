from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователя"

    def __str__(self):
        return f"Пользователь: {self.first_name} {self.last_name}"
