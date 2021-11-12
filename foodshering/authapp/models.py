from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Profile,
#  Пройти тест для подтверждженеи аккаунта
# Электронная почта
# Имя и фамилия, отчество
# Город
# Основной адрес (улица и дом)
# Ссылка на страницу «ВКонтакте»
# Телефон
# Дата рождения
#
#
class UserProfile(AbstractUser):
    class Status(models.TextChoices):
        Volunteer = 'v', 'Волонтёр'
        Coordinator = 'c', 'Координатор'

    email = models.EmailField(verbose_name='Почта')
    first_name = models.CharField(verbose_name='Имя', max_length=128)
    last_name = models.CharField(verbose_name='Фамилия', max_length=128)
    status = models.CharField(verbose_name='Статус', choices=Status.choices, default=Status.Volunteer, max_length=1)
    confirm = models.BooleanField(verbose_name='Подтверждён', default=False)

    def __str__(self):
        return f'{self.username} | {self.first_name} | {self.last_name}'


class Anketa(models.Model):
    username = models.ForeignKey(UserProfile, verbose_name='пользователь', on_delete=models.PROTECT)
    patronymic = models.CharField(verbose_name='Отчество', max_length=128, blank=True)
    city = models.CharField(verbose_name='Город', max_length=128)
    address = models.CharField(verbose_name='Основной адрес (улица и дом)', max_length=128)
    vk = models.URLField(verbose_name='Ссылка на страницу «ВКонтакте»')
    phone = models.CharField(verbose_name='Номер телефона', max_length=128)
    birthday = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.username} | {self.address}'

    class Meta:
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкета'
