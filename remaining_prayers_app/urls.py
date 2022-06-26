from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('main.urls')),
    path('settings/', include('settings.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]
