from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),  # Includes all app URLs
        path('api/', include('base.api.urls')),  # Add API routes

]
