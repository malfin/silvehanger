from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from mainapp.forms import CreateGroupForm
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


def edit_group(request, pk):
    if request.user.status == 'c' or request.user.is_staff:
        group = get_object_or_404(Group, id=pk)
        if request.method == 'POST':
            form = CreateGroupForm(request.POST, instance=group)
            if form.is_valid():
                forms = form.save(commit=False)
                forms.user_coordintator = request.user
                forms.save()
                form.save_m2m()
                messages.success(request, 'Вы успешно изменили группу!')
                return HttpResponseRedirect(reverse('mainapp:cabinet'))
        else:

            form = CreateGroupForm(instance=group)
        context = {
            'title': 'Изменить группу',
            'form': form,
        }
        return render(request, 'mainapp/group/create.html', context)
    else:
        return HttpResponseRedirect(reverse('mainapp:index'))


def create_group(request):
    if request.user.status == 'c' or request.user.is_staff:
        if request.method == 'POST':
            form = CreateGroupForm(request.POST)
            if form.is_valid():
                forms = form.save(commit=False)
                forms.user_coordintator = request.user
                forms.save()
                form.save_m2m()
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


def delete_group(request, pk):
    group = get_object_or_404(Group, id=pk)
    group.delete()
    return HttpResponseRedirect(reverse('mainapp:cabinet'))


def about(request):
    return render(request, 'mainapp/about.html')


def organizations(request):
    return render(request, 'mainapp/organizations.html')


def participants(request):
    return render(request, 'mainapp/participants.html')
