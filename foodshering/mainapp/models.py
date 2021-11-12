from django.contrib.auth.models import AbstractUser
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
class Profile(models.Model):
    username = models.ForeignKey(AbstractUser, verbose_name='пользователь', on_delete=models.PROTECT)
    email = models.EmailField(verbose_name='Почта')
    first_name = models.CharField(verbose_name='Имя', max_length=128)
    last_name = models.CharField(verbose_name='Имя', max_length=128)
    fio = models.CharField(verbose_name='Имя', max_length=128)
