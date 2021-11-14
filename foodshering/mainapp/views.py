from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from authapp.forms import ChangePassword, ChangeForm
from mainapp.forms import CreateGroupForm, LoadFileForm
from mainapp.models import Group, LoadFiles


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


def group_info(request, pk):
    if request.user.is_staff:
        group = Group.objects.filter(id=pk)
        context = {
            'group': group,
            'page_title': 'информация о группе'
        }
        return render(request, 'mainapp/group/index.html', context)
    else:
        return HttpResponseRedirect(reverse('mainapp:cabinet'))


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


def profile(request):
    context = {
        'title': 'личные данные',
    }
    return render(request, 'mainapp/lk/profile/index.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = ChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно изменили профиль!')
            return HttpResponseRedirect(reverse('mainapp:profile'))
    else:
        form = ChangeForm(instance=request.user)
    context = {
        'title': 'изменить профиль',
        'form': form,
    }
    return render(request, 'mainapp/lk/profile/edit.html', context)


def change_password(request):
    if request.method == 'POST':
        form = ChangePassword(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Вы успешно изменили пароль!')
            return HttpResponseRedirect(reverse('mainapp:profile'))
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибку ниже!')
    else:
        form = ChangePassword(user=request.user)
    context = {
        'title': 'изменить пароль',
        'form': form,
    }
    return render(request, 'mainapp/lk/profile/edit.html', context)


def about(request):
    return render(request, 'mainapp/about.html')


def organizations(request):
    return render(request, 'mainapp/organizations.html')


def participants(request):
    return render(request, 'mainapp/participants.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = LoadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:cabinet'))
    else:
        form = LoadFileForm()

    return render(request, 'mainapp/lk/cabinet.html', {
        'form': form
    })
