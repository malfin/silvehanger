from django.db import models

from authapp.models import UserProfile


class Group(models.Model):
    name = models.CharField(verbose_name='название группы', max_length=128)
    users_volonter = models.ManyToManyField(UserProfile)
    user_coordintator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='coordinator')

    def __str__(self):
        return f'{self.name} | {self.users_volonter}'
