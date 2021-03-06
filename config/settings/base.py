from pathlib import Path
from decouple import config

# modulo local
from . import credentials


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ir3zp754mp%(wjzytbrs$h)*18p52_lqg!9d)7fp2-_$(lb&#p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# app local
LOCAL_APPS = [
    'apps.users',
]

# third apps
THIRD_APPS = [
    'rest_framework',
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'exceptions.exception_handler.custom_exception_handler',
    'NON_FIELD_ERRORS': 'error',
    'DEFAULT_AUTHENTICATION_CLASSES': ('apps.users.authentication.authorization.JWTAuthentication',)
}

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

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# Definimos el modulo User personalizado
AUTH_USER_MODEL = 'users.User'


# Configuraci??n de base de datos.
# Se importo el modulo credentials donde esta las credenciales para hacer una conexi??n 
# si no existe el modulo "credentials" cree uno nuevo con sus credenciales.


ENGINE = 'django.db.backends.mysql'
NAME_SCHEMA = credentials.NAME_SCHEMA
USERNAME = credentials.USERNAME
PASSWORD = credentials.PASSWORD
HOST = credentials.HOST
PORT = credentials.PORT

""" 
Se configuro una cuenta que sera manejada por el sistema y que enviara 
una notificaci??n (mensaje de correo) al administrador del sistema.

"""

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.googlemail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER') # Agregar cuenta gmail 
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD') # Agregar password
EMAIL_USE_TLS = True



