from django.shortcuts import render

from mainapp.models import Group


def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def cabinet(request):
    if Group.objects.filter(user_coordintator=request.user):
        group = Group.objects.filter(user_coordintator=request.user)
        content = {
            'title': 'Личный кабинет | координатора',
            'group': group,
        }
        return render(request, 'mainapp/lk/coordinator.html', content)
    elif request.user.is_staff:
        content = {
            'title': 'Личный кабинет | Администратор',
        }
        return render(request, 'mainapp/lk/admin.html', content)
    elif Group.objects.filter(users_volonter=request.user):
        group = Group.objects.filter(users_volonter=request.user)
        content = {
            'title': 'Личный кабинет | волонтёра',
            'group': group,
        }
        return render(request, 'mainapp/lk/volonter.html', content)
    else:
        content = {
            'title': 'Личный кабинет | Ошибка',
        }
        return render(request, 'mainapp/lk/error.html', content)


def about(request):
    return render(request, 'mainapp/about.html')


def organizations(request):
    return render(request, 'mainapp/organizations.html')


def participants(request):
    return render(request, 'mainapp/participants.html')
