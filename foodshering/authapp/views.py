from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import LoginForm, RegisterForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = LoginForm()
    content = {
        'title': 'Авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', content)


@login_required()
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('authapp:login'))


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            print(form.fields)
            form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        form = RegisterForm()

    context = {
        'title': 'регистрация',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)
