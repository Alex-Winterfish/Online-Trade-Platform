from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group


class CustomUser(AbstractUser):
    """Модель пользователя model: users.CustomUser"""

    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(
        max_length=35,
        verbose_name="Phone",
        null=True,
        blank=True,
        help_text="Введите номер телефона",
    )
    country = models.CharField(
        max_length=50, verbose_name="Страна", help_text="Введите страну"
    )
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",
        blank=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
