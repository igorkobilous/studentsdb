"""
Django settings for studentsdb project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
from django.conf import global_settings
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xwr3&0e0rgs!8viv9w&-1k4r^=&1(869kamt5+=gfn6^^b@+j+'

# SMTP
# email settings
# please, set here you smtp server details and your admin email
ADMIN_EMAIL = 'admin@studentsdb.com'
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'ihorkobilous@gmail.com'
EMAIL_HOST_PASSWORD = 'ROti-8rYRJTbSSfsEoqCQg'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

ADMINS = (('Ihor', 'ihorkobilous@gmail.com'), ('Ihor', 'ihorbilous@yandex.ru'))
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

PORTAL_URL = 'http://localhost:8000'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'registration',
    'social.apps.django_app.default',
    'students',
    'studentsdb',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'studentsdb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'studentsdb.context_processors.students_proc',
                'students.context_processors.groups_processor',
                'django.core.context_processors.request',
                'django.core.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'studentsdb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'USER': 'students_db_user',
        'PASSWORD': 'x8wer3',
        'NAME': 'students_db',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

USE_I18N = True

LANGUAGE_CODE = 'uk'

USE_L10N = True

USE_TZ = True

TIME_ZONE = 'UTC'

LANGUAGES = [
    ('uk', 'Ukraine'),
    ('en', 'English'),
    ('pl', 'Polski'),
]



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')

#crispy temlate
CRISPY_TEMPLATE_PACK = 'bootstrap3'

#TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
#        "django.core.context_processors.request",
#        "studentsdb.context_processors.students_proc",
#        )

REGISTRATION_OPEN = True

LOGIN_URL = 'users:auth_login'
LOGOUT_URL = 'users:auth_logout'

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_FACEBOOK_KEY = '1052578368137861'
SOCIAL_AUTH_FACEBOOK_SECRET = '09f6de7ca423dcd6b3bcd3ec08feee7b'

#settings for Logger
LOG_FILE = os.path.join(BASE_DIR, 'studentsdb.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s: %(message)s'
        },
        'simple': {
            'format': '%(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': False,
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'students.signals': {
            'handlers': ['console', 'file', 'mail_admins'],
            'level': 'INFO',
        },
        'students.views.contact_admin': {
            'handlers': ['console', 'file', 'mail_admins'],
            'level': 'INFO',
        }
    }
}

