from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [

    path('', mainapp.index, name='index'),
    path('cabinet/', mainapp.cabinet, name='cabinet'),

    path('cabinet/profile/', mainapp.profile, name='profile'),
    path('cabinet/profile/edit/', mainapp.edit_profile, name='edit_profile'),
    path('cabinet/profile/edit/change_password/', mainapp.change_password, name='change_password'),

    path('about/', mainapp.about, name='about'),
    path('organizations/', mainapp.organizations, name='organizations'),
    path('participants/', mainapp.participants, name='participants'),

    path('cabinet/group/index/<int:pk>/', mainapp.group_info, name='group_info'),
    path('cabinet/group/create/', mainapp.create_group, name='create_group'),
    path('cabinet/group/edit/<int:pk>/', mainapp.edit_group, name='edit_group'),
    path('cabinet/group/delete/<int:pk>/', mainapp.delete_group, name='delete_group'),

]
