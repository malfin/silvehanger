from django.db import models

from authapp.models import UserProfile


class Group(models.Model):
    name = models.CharField(verbose_name='название группы', max_length=128)
    users_volonter = models.ManyToManyField(UserProfile)

    def __str__(self):
        return self.name
