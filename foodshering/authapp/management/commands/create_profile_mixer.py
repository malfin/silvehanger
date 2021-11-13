import random

from django.core.management.base import BaseCommand

from authapp.models import UserProfile

last_name = (
    'Попова', 'Васильев', 'Горбачева', 'Громова', 'Устинова', 'Рыбаков', 'Иванов', 'Кочетков', 'Романова', 'Кошелев'
)

first_name = (
    'Алексей', 'Валерия', 'Лука', 'Амина', 'Вероника', 'Даниил', 'Мария', 'Дамир', 'Вероника', 'Михаил'
)
status = ('v', 'c')


class Command(BaseCommand):
    help = 'Create UserProfile'

    def handle(self, *args, **options):
        print('Введите 1/2 (1 - создать 20 пользователей, 2 - создать 1 суперпользователя)')
        number = input()
        if number == '1':
            i = 0
            while i <= 19:
                UserProfile.objects.create_user(
                    username=f'user{i + 1}',
                    password=f'user{i + 1}',
                    first_name=random.choice(first_name),
                    status=random.choice(status),
                    address='Пирогова 16',
                    phone_number='+79088280065',
                    last_name=random.choice(last_name),
                    email=f'user{i + 1}@mail.ru'
                )
                i += 1
            print('Пользователи успешно создан!')
        elif number == '2':
            UserProfile.objects.create_superuser('admin', password='admin')
            print('Супер-пользователь успешно создан: login: admin; password: pass')
