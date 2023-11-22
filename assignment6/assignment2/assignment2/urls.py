# urls.py in your main project

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('degree_checklist/', include('degree_checklist.urls')),
    # Add other app URLs as needed
]
