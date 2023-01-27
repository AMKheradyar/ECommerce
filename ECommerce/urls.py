from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('sell/', include('sell.urls')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
