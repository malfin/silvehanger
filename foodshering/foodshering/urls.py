from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mainapp.urls', namespace='mainapp')),

    path('donor/', include('donorapp.urls', namespace='donorapp')),

    path('coordinator/', include('coordinatorapp.urls', namespace='coordinatorapp')),

    path('admin/', include('adminapp.urls', namespace='adminapp')),

    path('panel/', admin.site.urls),
]
