from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserRoles:
    USER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    choices = (
        (USER, "Пользователь"),
        (ADMIN, "Админ"),
        (MODERATOR, "Модератор")
    )


class User(AbstractUser):
    #email = models.EmailField(unique=True)
    #age = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"Пользователь: {self.first_name} {self.last_name}"
