"""
Django settings for cards project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'cards.context_processors.config',
    'cards.context_processors.this_year',
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lgv46aajfw4_vsor3zrrwbuv*__uruv&uthdnkf2%u=e#9=zv2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'constance',
    'constance.backends.database',
    'rd_suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'paintstore',
    'cards',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cards.urls'

WSGI_APPLICATION = 'cards.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
if DEBUG:
    STATIC_URL = 'http://localhost/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

"""
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'media'),
    os.path.join(BASE_DIR, 'static'),
)
"""

#Suit
SUIT_CONFIG = {
    'ADMIN_NAME': 'Radicards',
    'HEADER_DATE_FORMAT': 'Y-m-d',
    'HEADER_TIME_FORMAT': 'H:i:s',
    'MENU_EXCLUDE': ('auth.group', 'auth'),
    'LIST_PER_PAGE': 20,
}

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_CONFIG = {
    'SITE_NAME': ('Radicards', "Your card site's name"),
    'ORGANIZATION_NAME': ('Radical Designs', "The name of your organization"),
    'TEMPLATE': ('radicards', "The template to use"),
    'NUM_CARDS': (10, "Number of templates on the homepage"),
    'ANALYTICS_CODE': ('', "Your analytics tracker code"),
    'META TAGS': ('', "Meta tags for your site's <head>"),
    'SHARE': ('Facebook, Twitter, Google+, Tumblr', "List the social networks for which you want buttons."),
    'FORM_FIELDS': ('sender_first_name, sender_last_name, sender_email, sender_postal_code, sender_referrer, sender_mailing_list, recipient_first_name, recipient_last_name, recipient_email, message', "Form fields available for the users to fill out"),
    'REQUIRED_FIELDS': ('sender_first_name, sender_email, recipient_first_name, recipient_email, message', "Required form fields"),
    'NUM_FEATURED': (0, 'The number of featured cards to display on the homepage.'),
    'TAGLINE': ('Your own meme generator!', "Your site's tagline as appears in the title bar."),
    'RD_CREDIT': (True, 'Check to display our credit at the bottom of your site.'),
    'INTRO': ('', 'The intro for your homepage goes here'),
}
