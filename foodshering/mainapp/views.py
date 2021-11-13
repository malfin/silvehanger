from django.shortcuts import render

from mainapp.models import Group


def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)
