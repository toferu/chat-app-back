"""
Django settings for chat_api project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from decouple import config
import dj_database_url
import ssl
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'chat',
    'channels',
    'channels_postgres',
    'daphne',
    'corsheaders',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'chat_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# WSGI_APPLICATION = 'chat_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost'
    },
    'channels_postgres': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost'
    }

}

db_from_env = dj_database_url.config(conn_max_age=800, conn_health_checks = True)
DATABASES['channels_postgres'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ASGI_APPLICATION = 'chat_api.asgi.application'

#local testing
# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels.layers.InMemoryChannelLayer"
#     }
# }

#Redis
# ssl_context = ssl.SSLContext()
# ssl_context.check_hostname = False

# heroku_redis_ssl_host = {
#     'address': [os.environ.get('REDIS_TLS_URL', 'rediss://localhost:6379')],
#     'ssl': ssl_context
# }

# CHANNEL_LAYERS = {
#     "default": {
#         'BACKEND': "channels_redis.core.RedisChannelLayer",
#         'CONFIG': {
#             "hosts":(heroku_redis_ssl_host) ,
#         },
#     },
# }

# ssl_context = ssl.SSLContext()
# ssl_context.check_hostname = False

# CHANNEL_LAYERS = {
#     "default": {
#         'BACKEND': "channels_redis.core.RedisChannelLayer",
#         'CONFIG': {
#             "hosts":({
#                 'address': os.environ.get('REDIS_TLS_URL'),
#                 'ssl': ssl_context
#         },)
#     }
#   }  
# }

from chat_api.monkeypatch import CustomSSLConnection
from urllib.parse import urlparse

url = urlparse(os.environ.get('REDIS_TLS_URL'))
context = ssl.SSLContext()
context.check_hostname = False
channel_settings = {
    'CHANNEL_LAYERS': {
        'default': {
            'BACKEND': 'channels_redis.core.RedisChannelLayer',
            'CONFIG': {
                "hosts": [
                    {
                        'host': url.hostname,
                        'port': url.port,
                        'connection_class': CustomSSLConnection,
                        'ssl_context': context,
                    }
                ],
            },
        },
    }
}

#channels_postgres
# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_postgres.core.PostgresChannelLayer',
#         'CONFIG': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': 'postgres',
#             'USER': 'postgres',
#             'PASSWORD': 'password',
#             'HOST': '127.0.0.1',
#             'PORT': '5432',
#             }
#         },
#     },

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": [os.environ.get('REDIS_TLS_URL', 'redis://localhost:6379')],
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient"
#         }
#     }
# }