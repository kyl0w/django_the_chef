from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.accounts.urls')), 
    path('menu/', include('apps.menu.urls')), 
    path('administration/', include('apps.administration.urls')),
]
