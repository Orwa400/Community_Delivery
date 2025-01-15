from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URLs
    path('stores/', include('core.urls')),  # Include the URLs from the 'core' app
]