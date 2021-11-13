from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mainapp.urls', namespace='mainapp')),

    path('account/', include('authapp.urls', namespace='authapp')),

    path('panel/', admin.site.urls),
]
