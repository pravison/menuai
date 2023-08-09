"""

Django settings for restaurant project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/

"""

from pathlib import Path
import os

from environ import Env



env = Env()
env.read_env()

#from django-tenant_schemas import DATABASE_ROUTER

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRETE_KEY', default='django-insecure-bejs+w3ng#ji1srf(v9*maep3f@86gm7lp*1=p(axd6-p!cp9a')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  #'RENDER' not in os.environ

ALLOWED_HOSTS = ["*"]


RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


LOGIN_URL = "/dashboard/login/"
LOGIN_REDIRECT_URL ="/"
LOGOUT_REDIRECT_URL ="/"


# Application definition
SHARED_APPS = (
    'django_tenants',
    'client.apps.ClientConfig',
    
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
)

TENANT_APPS =(
    'menu',
    'qrgenerator',
    'dashboard',
    'client.apps.ClientConfig',
    'django.contrib.contenttypes',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
)

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

TENANT_MODEL = "client.Client"
TENANT_DOMAIN_MODEL ="client.Domain"

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'restaurant.urls'
PUBLIC_SCHEMA_URLCONF = 'restaurant.urls_public'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR , 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'restaurant.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '0710abdi',
        'PORT': '5432',
    }
}

# import dj_database_url 

# DATABASES = {
#     'default': dj_database_url.parse(
#         'postgres://pravo:1ZPs6wO8GfYAirfgcZvaXDDijixcEN1p@dpg-cj4c7e5gkuvsl087e4v0-a.frankfurt-postgres.render.com/menuai_c3vr',
#         conn_max_age=600,
#         conn_health_checks=True,
#         engine='django_tenants.postgresql_backend'
#     )
# }

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

PUBLIC_SCHEMA_NAME = 'public'



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'    
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
#turn on whitenoise storage backend
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SHOW_PUBLIC_IF_NO_TENANT_FOUND = True

