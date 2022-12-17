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
    chat_id = models.CharField(verbose_name="Id чата", max_length=20)
    user_ud = models.CharField(verbose_name="Ud пользователя", max_length=20)
    user_id = models.CharField(null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
