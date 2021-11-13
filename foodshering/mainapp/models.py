from django.db import models
from authapp.models import UserProfile


class Question(models.Model):
    ProfileId = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Тест')
    Text = models.TextField(verbose_name='Текст вопроса')
    Weight = models.FloatField(default=1, verbose_name='Вес')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.Text


class Answer(models.Model):
    QuestionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    Text = models.CharField(max_length=300)
    IsRight = models.BooleanField()

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.Text


class Result(models.Model):
    ProfileId = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Тест')
    UserName = models.CharField(max_length=300, verbose_name="ФИО")
    DateTime = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Время завершения")
    Rating = models.FloatField(verbose_name="Проценты")

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
