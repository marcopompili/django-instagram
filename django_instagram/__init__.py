from django.conf import settings as user_settings
from . import settings as default_settings

class AppSettings:
    def __getattr__(self, name):
        # If the setting you want is filled by the user, let's use it.
        if hasattr(user_settings, name):
            return getattr(user_settings, name)

        # If the setting you want has a default value, let's use it.
        if hasattr(default_settings, name):
            return getattr(default_settings, name)

        raise AttributeError("'Settings' object has no attribute '%s'" % name)

settings = AppSettings()
