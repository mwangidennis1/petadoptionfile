"""
Django settings for petadoption_project project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENVIRONMENT = os.environ.get('ENVIRONMENT', default='development')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY ='_hby^8ja+*tg5ah^vwk5@4(+$b-#uf6rvhjq2sz%qh#q+y-e5u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    #Third-aprty apps
    'crispy_forms',
    'allauth',
    'allauth.account',
    #local
    'users.apps.UsersConfig',
    'pages.apps.PagesConfig',
    'animals.apps.AnimalsConfig',
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

ROOT_URLCONF = 'petadoption_project.urls'

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

WSGI_APPLICATION = 'petadoption_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER':'postgres',
        'PASSWORD' : 'postgres',
        'HOST': 'db',
        'PORT':5432

    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static'),]
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
STATICFILES_FINDERS = [
"django.contrib.staticfiles.finders.FileSystemFinder", 
"django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

AUTH_USER_MODEL = 'users.CustomUser' 
LOGIN_REDIRECT_URL='animal_list'
ACCOUNT_LOGOUT_REDIRECT='animal_list'
CRISPY_TEMPLATE_PACK='bootstrap4'
#django-allauth config
SITE_ID=1
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_EMAIL_REQUIRED = True 
ACCOUNT_UNIQUE_EMAIL = True 
#ACCOUNT_CONFIRM_EMAIL_ON_GET=True
AUTHENTICATION_BACKENDS = (
'django.contrib.auth.backends.ModelBackend', 
'allauth.account.auth_backends.AuthenticationBackend', 
)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
#EMAIL_HOST='smtp.gmail.com'
#EMAIL_USE_TLS=True
#EMAIL_PORT=587
#MAIL_HOST_USER='mwangedennis05@gmail.com'
#EMAIL_HOST_PASSWORD='hnsy gksw ukce utwn'
#DEFAULT_FROM_EMAIL = 'admin@petadoption.com'

#media config
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')