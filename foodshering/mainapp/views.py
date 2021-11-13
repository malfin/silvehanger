from django.shortcuts import render

from mainapp.models import Group


def index(request):
    group = Group.objects.filter(users_volonter=request.user)
    context = {
        'title': 'главная',
        'group': group,
    }
    return render(request, 'mainapp/index.html', context)
