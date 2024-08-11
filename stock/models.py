from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название склада')
    address = models.CharField(max_length=256, verbose_name='Адрес склада')
    phone = models.CharField(max_length=128, verbose_name='Телефон склада')
    email = models.CharField(max_length=128, verbose_name='Email склада')


class Category(models.Model):
    category = models.CharField(max_length=256, verbose_name='Категория оборудования')
    info = models.TextField(verbose_name='Информация о категории')


class Equipment(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название оборудования')
    number = models.CharField(max_length=128, verbose_name='Серийный номер')
    age = models.CharField(max_length=128, verbose_name='Дата выпуска')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")
    image = models.ImageField(upload_to='image', verbose_name='Фотография оборудования')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    stock = models.ForeignKey('Stock', on_delete=models.PROTECT, verbose_name='Склад хранения')
