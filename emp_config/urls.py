from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employee.urls')),
    path('accounts/', include('accounts.urls')),
    path('profile/', include('profiles.urls')),
]
