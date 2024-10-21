from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('referrals.urls', namespace='referrals')),
    path('users/', include('users.urls', namespace='users')),
]
