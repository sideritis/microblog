import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pkr48ibeu0(=wh2g2nbkeugasq+x)e8lz4+b9u)ymh(6i(#2o3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = '127.0.0.1'
DOMAIN = 'http://127.0.0.1:8000'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps
    'corsheaders',
    'markdownx',
    'captcha',
    'django_cleanup',
    'rest_framework',
    'rest_framework.authtoken',
    'solo',
    'easy_thumbnails',
    # My apps
    'account',
    'article',
    'tag',
    'guest_book',
    'other',
    'core',
    'file',
    'api',
    'newsletter'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'microblog.urls'

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
                'microblog.context_processors.navigation',
                'microblog.context_processors.settings',
                'microblog.context_processors.footer',
                'microblog.context_processors.site_meta'
            ],
        },
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

CACHE_TIME = 60 * 60 * 48

WSGI_APPLICATION = 'microblog.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db1.sqlite3'),
    }
}


# Password validation

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
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'templates', 'static')
]

AUTH_USER_MODEL = 'account.User'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Names reserved for apps etc.
PROHIBITED_NAMES = ['author', 'tag', 'guest_book', 'other', 'file', 'api', 'lang']

# Project version
VERSION = '0.12.6'

CORS_ORIGIN_ALLOW_ALL = True

# Rest config
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

# Date
DATE_FORMAT = "j N Y"

# Markdownx setup
MARKDOWNX_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra'
]

# This must be always at the of file
DEV_APPS = None

THUMBNAIL_ALIASES = {
    '': {
        'article_thumbnail': {'size': (800, 80), 'crop': True},
    },
}

# Email setup
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.example.net'
EMAIL_HOST_USER = 'example_username'
EMAIL_HOST_PASSWORD = 'example_password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL = 'admin@example.com'

try:
    from .local_settings import *
    INSTALLED_APPS += DEV_APPS
except ImportError:
    pass

try:
    from .production_settings import *
except ImportError:
    pass

