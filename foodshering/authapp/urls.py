from django.urls import path

import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [

    path('login/', authapp.login, name='login'),

    path('logout/', authapp.logout, name='logout'),

    path('register/', authapp.register, name='register'),

    path('confirm_user/<int:pk>', authapp.confirm_user, name='confirm_user'),

]
