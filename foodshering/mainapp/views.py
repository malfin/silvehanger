from django.shortcuts import render

from mainapp.models import Group


def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def lk(request):
    if Group.objects.filter(users_volonter=request.user):
        group = Group.objects.filter(users_volonter=request.user)
        content = {
            'title': 'Личный кабинет | волонтёра',
            'group': group,
        }
        return render(request, 'mainapp/lk/volonter.html', content)
    elif request.user.is_staff:
        content = {
            'title': 'Личный кабинет | Администратор',
        }
        return render(request, 'mainapp/lk/admin.html', content)
    elif Group.objects.filter(user_coordintator=request.user):
        group = Group.objects.filter(user_coordintator=request.user)
        content = {
            'title': 'Личный кабинет | координатора',
            'group': group,
        }
        return render(request, 'mainapp/lk/coordinator.html', content)
