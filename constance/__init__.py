from constance.config import Config

#config = Config()
try:
    from django.apps import AppConfig
except ImportError:
    config = Config()
else:
    default_app_config = 'constance.apps.ConstanceConfig'
