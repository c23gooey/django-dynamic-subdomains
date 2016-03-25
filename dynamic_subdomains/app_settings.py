from django.conf import settings

def setting(name, default):
    @property
    def fn(self):
        return getattr(settings, name, default)
    return fn

class AppSettings(object):
    SUBDOMAINS = setting('SUBDOMAINS', ())
    DEFAULT_SUBDOMAIN = setting('DEFAULT_SUBDOMAIN', None)

    PROTOCOL = setting('SUBDOMAINS_PROTOCOL', 'http')

    EMULATE = setting('EMULATE_SUBDOMAINS', settings.DEBUG)
    COOKIE_NAME = setting('SUBDOMAINS_COOKIE_NAME', 'dynamic-subdomains-host')
    EMULATE_BASE_URL = setting('EMULATE_BASE_URL', 'http://127.0.0.1:8000')

app_settings = AppSettings()
