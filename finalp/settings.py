"""
Django settings for finalp project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates") 
STATIC_DIR = os.path.join(BASE_DIR, "static") 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '54ps(t^to1lmmtd_*^)s4sa%=eaa-+cqjs=q2y0h50&#og#t3z'

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
    'final_app',
    'backend',
    'blog',
    'crispy_forms',
    'tinymce',
]

TINYMCE_DEFAULT_CONFIG = { 
    'height': 360, 
    'width': 1120, 
    'cleanup_on_startup': True, 
    'custom_undo_redo_levels': 20, 
    'selector': 'textarea', 
    'theme': 'modern', 
    'plugins': ''' 
            textcolor save link image media preview codesample contextmenu 
            table code lists fullscreen  insertdatetime  nonbreaking 
            contextmenu directionality searchreplace wordcount visualblocks 
            visualchars code fullscreen autolink lists  charmap print  hr 
            anchor pagebreak 
            ''', 
    'toolbar1': ''' 
            fullscreen preview bold italic underline | fontselect, 
            fontsizeselect  | forecolor backcolor | alignleft alignright | 
            aligncenter alignjustify | indent outdent | bullist numlist table | 
            | link image media | codesample | 
            ''', 
    'toolbar2': ''' 
            visualblocks visualchars |
             charmap hr pagebreak nonbreaking anchor |  code | 
            ''', 
    'contextmenu': 'formats | link image', 
    'menubar': True, 
    'statusbar': True, 
    } 

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'finalp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'finalp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR]
MEDIA_URL = '/media/'


LOGIN_REDIRECT_URL = 'blog:list'


EMAIL_FILE_PATH = os.path.join(BASE_DIR,"sent_emails")
SEND_GRID_API_KEY = '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'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'waju'
EMAIL_HOST_PASSWORD = 'lanre7912'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'lanre7912@gmail.com'
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'Contact email received from learnIT'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'