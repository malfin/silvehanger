from django.shortcuts import render

from mainapp.models import Group


def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def cabinet(request):
    if Group.objects.filter(users_volonter=request.user):
        group = Group.objects.filter(users_volonter=request.user)
        content = {
            'title': 'Личный кабинет | Волонтёр',
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
            'title': 'Личный кабинет | Координатор',
            'group': group,
        }
        return render(request, 'mainapp/lk/coordinator.html', content)
    else:
        content = {
            'title': 'Личный кабинет | Ошибка',
        }
        return render(request, 'mainapp/lk/error.html', content)


def about(request):
    content = {
        'title': 'Фудшеринг | О нас',
    }
    return render(request, 'mainapp/about.html', content)


def organizations(request):
    content = {
        'title': 'Фудшеринг | Организациям',
    }
    return render(request, 'mainapp/organizations.html', content)


def participants(request):
    content = {
        'title': 'Фудшеринг | Учасникам',
    }
    return render(request, 'mainapp/participants.html', content)
