from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    username = None
    telegram_id = models.CharField(max_length=100, verbose_name="ник в телеграм")
    email = models.EmailField(unique=True, verbose_name="электронная почта")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["telegram_id"]

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"

    def get_full_name(self) -> str:
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        ordering = None
