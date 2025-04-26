from django.conf import settings
from django.contrib import admin
from django.urls import path
from apps.user_auth.views import TestLoggerView
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("", TestLoggerView.as_view(), name="test_logger"),
    # Add other URL patterns here
]
