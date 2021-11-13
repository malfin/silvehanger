from django.db import models

from authapp.models import UserProfile


class Group(models.Model):
    name = models.CharField(verbose_name='название группы', max_length=128)
    users_volonter = models.ManyToManyField(UserProfile)
    user_coordintator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='coordinator')

    def __str__(self):
        return f'{self.name}, Координатор: {self.user_coordintator.username}'


class Product(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Благотворитель')
    name = models.CharField(verbose_name='Наименование', max_length=64)
    colicestvo = models.FloatField(verbose_name='Количество/вес')
    price = models.FloatField(verbose_name='Цена')
    srok = models.DateField(verbose_name='Срок годности')
    desc = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user}, Продукт: {self.name}'
