from django.conf import settings
from django.contrib import admin
from django.urls import path
from apps.user_auth.views import TestLoggerView
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    # Add other URL patterns here
]
