from django.db import models
from django.contrib.auth.models import AbstractUser


# Создание пользовательской модели CustomUser
class CustomUser(AbstractUser):
    # Поле username для имени пользователя
    username = models.CharField(max_length=150, default='')
    # Поле email для адреса электронной почты пользователя
    email = models.EmailField(unique=True)

    # Задаем поле email как основное поле для входа в систему
    USERNAME_FIELD = 'email'
    # Требуем указание поля username при создании пользователя
    REQUIRED_FIELDS = ['username']

    # Метод str для строкового представления объекта CustomUser
    def __str__(self):
        return self.username
