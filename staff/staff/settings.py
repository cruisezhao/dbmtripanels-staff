"""
Django settings for staff project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import socket
from django.urls import reverse_lazy
hostname = socket.gethostname()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)),'common')
STATICFILES_DIRS = [os.path.join(STATIC_DIR, 'static')]
MEDIA_ROOT = os.path.join(BASE_DIR,'media')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '3@+wn)qdzs3i@u#rc9@jlw__n7u@3y)c#2x#$%9fhln3-70s@s'
SECRET_KEY = 'f5l(t&w_k34o%zg!od8h+3f11by!v_)l*jydv#(t986mi27swu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'common.apps.users',
    #dependeny used for ticket
    'django.contrib.sites',
    #{#load humanlize#}
    'django.contrib.humanize',
    'common.apps.utiltemplate',
    'common.apps.clients',
    'common.apps.packages',
    'common.apps.products',
    'common.apps.orders',
    'common.apps.deployments',
    'common.apps.infrastructure',

    'authtools',
    'crispy_forms',
    'django_filters',
    'django_tables2',
    'crudbuilder',
    #'staff',
    'bootstrapform',
    'helpdesk',
    'widget_tweaks',
    'rest_framework',
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

ROOT_URLCONF = 'staff.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'staff.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

if hostname == 'LAPTOP-TJHAEPAJ':
    DATABASES = {
        'default': {
            # 'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
             #Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
             'ENGINE': 'django.db.backends.mysql',
             # Or path to database file if using sqlite3.
             'NAME': 'tripanels',
             'USER': 'root',                      # Not used with sqlite3.
             'PASSWORD': 'mysql.com',                  # Not used with sqlite3.
             # Set to empty string for localhost. Not used with sqlite3.
             'HOST': 'localhost',
             # Set to empty string for default. Not used with sqlite3.
             'PORT': '3306',
             #'OPTIONS': {'init_command': 'SET storage_engine=INNODB;'}
        }
    }
elif hostname == 'LAPTOP-UAJH5H4I':
    DATABASES = {
        'default': {
            # 'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
             #Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
             'ENGINE': 'django.db.backends.mysql',
             # Or path to database file if using sqlite3.
             'NAME': 'tripanel',
             'USER': 'root',                      # Not used with sqlite3.
             'PASSWORD': 'tripanels',                  # Not used with sqlite3.
             # Set to empty string for localhost. Not used with sqlite3.
             'HOST': 'localhost',
             # Set to empty string for default. Not used with sqlite3.
             'PORT': '3306',
             #'OPTIONS': {'init_command': 'SET storage_engine=INNODB;'}
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'tripanels', #Your db name
            'USER': 'tripanels', #Your db user name
            'PASSWORD':'Data8ase-tripanels',
            'HOST':'45.35.50.34',
            'PORT':'3306',
        }
    }



# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = reverse_lazy('home')
LOGOUT_REDIRECT_URL = reverse_lazy('users:login')
LOGIN_URL = reverse_lazy('users:login')
AUTH_USER_MODEL = 'users.Users'

if hostname == 'cluster':
    SESSION_COOKIE_DOMAIN = '.tripanels.com'
else:
    SESSION_COOKIE_DOMAIN = None

AUTHENTICATION_BACKENDS = ['common.apps.users.backends.AllowStaffGroupUsersModelBackend']

#tickets
SITE_ID = 2

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

#crudbuilder
LOGIN_REQUIRED_FOR_CRUD = True
PERMISSION_REQUIRED_FOR_CRUD = False
PROJECT_NAME = 'staff'

PAGINATE_COUNT = 2

#test base path for api
BASE_PATH = "http://127.0.0.1:8000/"