"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

from django.contrib.messages import constants as messages
# import environ

# env = environ.Env( DEBUG=(bool, False)
# )
# environ.Env.read_env()

MESSAGE_TAGS = {
        messages.DEBUG: 'secondary',
        messages.INFO: 'info',
        messages.SUCCESS: 'success',
        messages.WARNING: 'warning',
        messages.ERROR: 'danger',
}
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)k-93y5@h@bk*y*34wad2mk18vaa=bln_w1xr9+rq(#p_g6s$n'
# SECRET_KEY = env("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'intern',
    'blog',
    'sslserver',
    'social_django',
    'file_uploader',
    'taggit',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


#auth account extend auth_user of django
AUTH_USER_MODEL = 'accounts.Account'
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'quocbao',
        'PASSWORD': 'voquocbao',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
# DATABASES = { 
#         "default": { 
#             "ENGINE": env("DATABASE_ENGINE"), 
#             "NAME": env("DATABASE_NAME"), 
#             "USER": env("DATABASE_USER"), 
#             "PASSWORD": env("DATABASE_PASSWORD"), 
#             "HOST": env("DATABASE_HOST"), 
#             "PORT": env("DATABASE_PORT"), 
#             }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

#auth social account in web
AUTHENTICATION_BACKENDS = [
    'social_core.backends.facebook.FacebookOAuth2',
    
    'django.contrib.auth.backends.ModelBackend',
    
]

USER_FIELDS = ['email','first_name', 'last_name'] 
#Login by Facebook 
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SOCIAL_AUTH_FACEBOOK_KEY = '541042307247359'       # App ID
SOCIAL_AUTH_FACEBOOK_SECRET ='8149a1f64f9ea3ba366e3c9bb531b936'  #APP_Secret


SESSION_COOKIE_SAMESITE = None
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Ho_Chi_Minh'
# LANGUAGE_CODE = env("LANGUAGE_CODE")
# TIME_ZONE = env("TIME_ZONE")

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    
]

MEDIA_URL = '/media/images/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

VENDORS_URL = '/vendors/fonts/webfonts'
VENDORS_ROOT = os.path.join(BASE_DIR,'vendors')

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/blog/'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'

#Email activate 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'voquocbaonana@gmail.com'
EMAIL_HOST_PASSWORD = 'voquocbao'
EMAIL_PORT = 587