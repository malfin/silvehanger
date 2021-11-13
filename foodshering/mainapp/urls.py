from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [

    path('', mainapp.index, name='index'),
    path('cabinet/', mainapp.cabinet, name='cabinet'),
    path('about/', mainapp.about, name='about'),
    path('organization/', mainapp.organizations, name='organizations'),
    path('participant/', mainapp.participants, name='participants'),

]
