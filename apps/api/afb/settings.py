"""
Django settings for afb project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# When using Django Rest Framework (DRF), you typically don't use
# LOGIN_REDIRECT_URL because DRF is designed to build APIs, which are
# generally stateless. This means after a successful login, instead of
# redirecting to a new page, you would return a response (often with a token
# for authentication).

# However, if you're building a browsable API with DRF and want to redirect
# after login, you can set LOGIN_REDIRECT_URL to any valid URL endpoint in
# your Django project. This could be a DRF view that returns JSON data, or a
# Django view that returns HTML.
LOGIN_REDIRECT_URL = "/api/users/current_user/"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-k3nma!u)7oz(lt346n-=rx=rt%u_^j8-rdz3p(y3o$ot0%soqh"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
# http://127.0.0.1:8000/static/src/assets/logo.png

INSTALLED_APPS = [
    "unfold",  # https://github.com/unfoldadmin/django-unfold
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",  # add this for 'python manage.py runserver_plus'
    "rest_framework",  # add DRF
    "django_filters",  # add DRF filters
    "phonenumber_field",
    "django_vite",  # May not need this? If using Vite/Vue for frontend via API.
    "afbcore",
]

VITE_APP_DIR = BASE_DIR.parent / "ui"

# correspond to your build.outDir in your ViteJS configuration.
DJANGO_VITE_ASSETS_PATH = VITE_APP_DIR / "dist"

# ViteJS webserver protocol (default : http).
DJANGO_VITE_DEV_SERVER_PROTOCOL = "http"

# ViteJS webserver hostname (default : localhost).
DJANGO_VITE_DEV_SERVER_HOST = "127.0.0.1"

# ViteJS webserver port (default : 3000)
DJANGO_VITE_DEV_SERVER_PORT = "3000"

# assets are included as modules using the ViteJS webserver. This will enable
# HMR for your assets.
DJANGO_VITE_DEV_MODE = True

# ViteJS webserver path to the HMR client used in the vite_hmr_client tag
# (default : @vite/client).
DJANGO_VITE_WS_CLIENT_URL = "@vite/client"

# Absolute path (including filename) to your ViteJS manifest file. This
# file is generated in your DJANGO_VITE_ASSETS_PATH. But if you are in
# production (DEBUG is false) then it is in your STATIC_ROOT after you
# collected your static files (supports pathlib.Path or str).
DJANGO_VITE_MANIFEST_PATH = DJANGO_VITE_ASSETS_PATH / "manifest.json"

# prefix directory of your static files built by Vite. (default : "")
# Use it if you want to avoid conflicts with other static files in your project.
DJANGO_VITE_STATIC_URL_PREFIX = ""

VITE_INPUT_CSS = "input.css"
VITE_OUTPUT_CSS = "output.css"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-STATIC_ROOT
# https://docs.djangoproject.com/en/4.2/howto/static-files/#deployment
# This should be an initially empty destination directory. it is not a place
# to store your static files permanently.
STATIC_ROOT = BASE_DIR / "staticfiles"

# For prod:
# https://docs.djangoproject.com/en/4.2/howto/static-files/deployment/#staticfiles-from-cdn
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-STORAGES
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
    VITE_APP_DIR / "dist",
    VITE_APP_DIR / "public",
    DJANGO_VITE_ASSETS_PATH,
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
}

PHONENUMBER_DB_FORMAT = "INTERNATIONAL"
PHONENUMBER_DEFAULT_FORMAT = "E164"
PHONENUMBER_DEFAULT_REGION = "CA"


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "afb.urls"

# Django-Tailwind
# https://django-tailwind.readthedocs.io/en/latest/installation.html#configuration

# TAILWIND_APP_NAME = "theme"

AUTH_USER_MODEL = "afbcore.User"

INTERNAL_IPS = [
    # Add local IP addresses here for tailwind to work, then run:
    # * (Dev) `python manage.py tailwind install`
    # * (Production) `python manage.py tailwind build`
    "127.0.0.1",
]

# Templates
# https://docs.djangoproject.com/en/4.2/ref/settings/#templates

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "afb.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
