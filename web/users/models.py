from django.db import models
from django.contrib.auth.models import AbstractUser


class ImpUser(AbstractUser):
    """Whole Imperial system 'User' model"""
    USER_GENDER = (
        ('m', "Мужской"),
        ('f', "Женский")
    )

    first_name = models.CharField(max_length=100, verbose_name="Имя")
    second_name = models.CharField(max_length=100, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=100, verbose_name="Отчество")
    birth_date = models.DateField(blank=True, verbose_name="Дата рождения")
    birth_place = models.CharField(max_length=100, help_text="Страна, город", blank=True, verbose_name="Место рождения")
    username = models.CharField(unique=True, max_length=50, blank=False, verbose_name="Псевдоним")
    password = models.CharField(max_length=100, verbose_name="Пароль")
    private_email = models.EmailField(max_length=250, blank=False, verbose_name="Основная электронная почта")
    operation_email = models.EmailField(max_length=250, blank=True, verbose_name="Операционная электронная почта")
    phone_number = models.CharField(max_length=15, blank=True, unique=True, verbose_name="Номер телефона")
    add_phone_number = models.CharField(max_length=15, blank=True, unique=True,
                                        verbose_name="Дополнительный номер телефона")
    gender = models.CharField(max_length=1, choices=USER_GENDER, blank=False, verbose_name="Пол")
    profile_image = models.ImageField(upload_to="media/uploads/users/avatars/", blank=True, verbose_name="Фото профиля")
    balance_accounts = models.ManyToManyField("finances.ImpBalance", blank=True, verbose_name="Счета")
    # TODO: Create multiple passport data classes var(ManyToMany)


