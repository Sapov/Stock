from django.contrib.auth import get_user_model
from django.db import models

from django.contrib.auth.models import Group, User


class Stock(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название склада")
    address = models.CharField(max_length=256, verbose_name="Адрес склада")
    phone = models.CharField(max_length=128, verbose_name="Телефон склада")
    email = models.CharField(max_length=128, verbose_name="Email склада")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Склады"
        verbose_name = "Склад"


class Category(models.Model):
    category = models.CharField(max_length=256, verbose_name="Категория оборудования")
    info = models.TextField(verbose_name="Информация о категории")

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категория"


class Equipment(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название оборудования")
    number = models.CharField(max_length=128, verbose_name="Серийный номер")
    age = models.DateField(max_length=128, verbose_name="Дата выпуска")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")
    image = models.ImageField(upload_to="image", verbose_name="Фотография оборудования")
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, verbose_name="Категория"
    )
    stock = models.ForeignKey(
        "Stock", on_delete=models.PROTECT, verbose_name="Склад хранения"
    )
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Владелец оборудования"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Оборудование"
        verbose_name = "Оборудование"
