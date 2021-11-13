from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from mainapp.forms import LoadFileForm, CreateGroupForm
from mainapp.models import Group


def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def cabinet(request):
    if request.user.status == 'c':
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
    elif request.user.status == 'v':
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


def create_group(request):
    if request.user.status == 'c':
        if request.method == 'POST':
            form = CreateGroupForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Вы успешно создали группу!')
                return HttpResponseRedirect(reverse('mainapp:cabinet'))
        else:
            form = CreateGroupForm()
        context = {
            'title': 'Добавить группу',
            'form': form,
        }
        return render(request, 'mainapp/group/create.html', context)
    else:
        return HttpResponseRedirect(reverse('mainapp:index'))


def about(request):
    return render(request, 'mainapp/about.html')


def organizations(request):
    return render(request, 'mainapp/organizations.html')


def participants(request):
    return render(request, 'mainapp/participants.html')
