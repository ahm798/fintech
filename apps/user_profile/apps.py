from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _  

class UserProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.user_profile'
    verbose_name = _('User Profile')
    label = 'user_profile'
    path = 'apps/user_profile'
