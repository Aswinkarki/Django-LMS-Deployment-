"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&k7um+nu0)^i_d!j&*$-0%*+1(%-i0*2tpgm9uzisue2irv2%e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'send-overdue-emails-every-day': {
        'task': 'dashboard.tasks.send_overdue_emails',
        'schedule': crontab(hour=8, minute=0),  # Run daily at 8 AM UTC
    },
}

# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'whitenoise.runserver_nostatic',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'rest_framework',
     'django_celery_beat',
    'rest_framework_simplejwt',
    'Users',
    'Authors',
    'Students',
    'Transactions',
    'Books',
    'Dashboard',
]
from datetime import timedelta
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ALLOW_ALL_ORIGINS = True 

ROOT_URLCONF = 'myproject.urls'

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


# ALLOWED_HOSTS = ['aswin.kutumbatech.com.np',
#     'aswin.kutumbatech.com.np:5009',
# ]
ALLOWED_HOSTS = ['*']


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "gartaulapratiksha81@gmail.com"
EMAIL_HOST_PASSWORD = "poxx dpey vqfu qgbd"  # Replace this with your Gmail App Password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         # 'NAME': 'yoo',
#         # 'USER': 'postgres',
#         # 'PASSWORD': 'xxx',
#         # 'HOST': 'db',  # Change if using a remote database
#         # 'PORT': '5432',       # Default PostgreSQL port
#         'NAME': 'Library',  # Your database name
#         'USER': 'postgres',  # PostgreSQL username (default is 'postgres')
#         'PASSWORD': 'Aswin',  # Your PostgreSQL password
#         'HOST': 'db',  # Use 'localhost' if PostgreSQL is running locally
#         'PORT': '5432',  # Default PostgreSQL port
#     }
# }
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'LibraryMgmt',
        'USER': 'mysuperuser',
        'PASSWORD': 'mysuperuser',
        'HOST': 'librarymgmt.czsismkgq1w8.us-east-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DB_NAME', 'Library'),
#         'USER': os.environ.get('DB_USER', 'postgres'),
#         'PASSWORD': os.environ.get('DB_PASSWORD', 'Aswin'),
#         'HOST': os.environ.get('DB_HOST', 'postgres'),
#         'PORT': os.environ.get('DB_PORT', '5432'),
#     }
# }


# Celery Configuration
# CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Redis as the broker
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'UTC'

CELERY_BROKER_URL = 'pyamqp://guest:guest@localhost//'  # RabbitMQ as the broker
CELERY_RESULT_BACKEND = 'rpc://'  # Use 'rpc://' or disable result backend if not needed
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

#Aswinkarki
#Aswinkarki123


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'Users.User'

from datetime import timedelta

SIMPLE_JWT = {
    'USER_ID_FIELD': 'userId',  # Use the correct primary key field name
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=2), 
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=5),  
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



LOGS_DIR = os.path.join(BASE_DIR, 'logs')  # Path to logs folder

if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)  # Ensure logs directory exists
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.core.mail': {  # Add this to log email sending
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

from decouple import config

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'djangolms'
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'us-east-2'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERIFY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'