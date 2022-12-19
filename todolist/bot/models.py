from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone


class BaseModelBot(models.Model):
    created = models.DateTimeField(verbose_name="Дата создания")

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super().save(*args, **kwargs)


class Bot(BaseModelBot):
    chat_id = models.BigIntegerField()
    user_id = models.BigIntegerField(unique=True)
    user_ud = models.CharField(max_length=40, validators=[MinLengthValidator(5)])
    user = models.ForeignKey("core.User", null=True, on_delete=models.CASCADE)
    verification_code = models.CharField(max_length=15, unique=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
