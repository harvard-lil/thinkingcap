"""
Django settings for thinkingcap project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f#ong^2euz5kcnk6)46%8)hn51sm($23is7rx&go$d@wmfw-+n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'onthisday',
    'colors',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'thinkingcap',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    },

}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# ======================== #
#           EMAIL          #
# ======================== #
ADMIN_EMAIL_ADDRESS = 'main-email-address@example.com'
EMAIL_ADDRESS = 'admin-email-address@example.com'

EMAIL_USE_TLS = True
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST_PASSWORD = '123'
EMAIL_HOST_USER = 'user-secret'
EMAIL_HOST_PASSWORD = 'secret-secret'


# ======================== #
#       API SETTINGS       #
# ======================== #
API_BASE_URL = "http://localhost:8000/api/v1/"
# until we open up the api to everyone, we need to pass in a certificate with every prod request
API_CERT_REQUIRED = False
API_PEM_CERT = "cert.pem"
API_PEM_KEY = "key.pem"

# ======================== #
#     APP SPECIFIC KEYS    #
# ======================== #

#          colors
# ==========================
# API TOKEN used for colors app
API_TOKEN_COLORS = '123'
API_LIMIT_COLORS = 500

# taken from https://simple.wikipedia.org/wiki/List_of_colors
COLOR_LIST = [
    "amaranth", "amber", "amethyst", "apricot", "aquamarine", "azure", "baby blue", "beige", "black", "blue", "blue green",
    "blue violet", "blush", "bronze", "brown", "burgundy", "byzantium", "carmine", "cerise", "cerulean", "champagne",
    "chartreuse green", "chocolate", "cobalt blue", "coffee", "copper", "coral", "crimson", "cyan", "desert sand",
    "electric blue", "emerald", "erin", "gold", "gray", "green", "harlequin", "indigo", "ivory", "jade", "jungle green",
    "lavender", "lemon", "lilac", "lime", "magenta", "magenta rose", "maroon", "mauve", "navy blue", "ocher", "olive", "orange",
    "orange red", "orchid", "peach", "pear", "periwinkle", "persian blue", "pink", "plum", "prussian blue", "puce", "purple",
    "raspberry", "red", "red violet", "rose", "ruby", "salmon", "sangria", "sapphire", "scarlet", "silver", "slate gray",
    "spring bud", "spring green", "tan", "taupe", "teal", "turquoise", "violet", "viridian", "white", "yankees blue", "yellow"
]

#        onthisday
# ==========================
API_TOKEN_ONTHISDAY = '456'
START_YEAR_ONTHISDAY = 1650
EMAIL_ONTHISDAY = 'example@gmail.com'