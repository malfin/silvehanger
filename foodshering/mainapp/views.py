from django.shortcuts import render

from mainapp.models import Group


def index(request):
    group = Group.objects.filter(users__group=request.user)
    context = {
        'title': 'группа',
        'group': group,
    }
    return render(request, 'mainapp/group/index.html')
