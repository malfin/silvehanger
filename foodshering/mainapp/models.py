from django.db import models
from django.core.validators import RegexValidator
from authapp.models import UserProfile


class Group(models.Model):
    name = models.CharField(verbose_name='название группы', max_length=128)
    users_volonter = models.ManyToManyField(UserProfile)
    user_coordintator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='coordinator')

    def __str__(self):
        return f'{self.name}, Координатор: {self.user_coordintator.username}'


class Organ(models.Model):
    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=('Необходимо ввести номер телефона в формате: +70123456789, '
                 'допускается до 15 знаков')
    )

    name = models.CharField(verbose_name='Наименование', max_length=64)
    address = models.CharField(verbose_name='Адрес', max_length=128)
    phone_number = models.CharField(validators=[phone_validator], max_length=17, verbose_name="Номер организации")
    email = models.EmailField(max_length=200, verbose_name='Почта')
    personal = models.CharField(verbose_name='Сотрудник организации', max_length=64)


class Product(models.Model):
    org_id = models.ForeignKey(Organ, on_delete=models.CASCADE, related_name='organ')
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group')
    name = models.CharField(verbose_name='Наименование', max_length=64)
    colicestvo = models.IntegerField(verbose_name='Количество')
    ves = models.FloatField(verbose_name='вес')
    price = models.FloatField(verbose_name='Цена')
    srok = models.DateField(verbose_name='Срок годности')
    desc = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'


class LoadFiles(models.Model):
    file = models.FileField(verbose_name='файл', upload_to='file')
    date = models.DateField(verbose_name='дата загрузки', auto_now=True)

    def __str__(self):
        return f'{self.date}'
