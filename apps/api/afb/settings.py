"""
Django settings for afb project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Load dotenv file
from dotenv import load_dotenv

# After loading dotenv, you can use os.getenv() to access
# environment variables. e.g. `os.getenv("DEBUG", "False")`
load_dotenv()


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
LOGIN_REDIRECT_URL = os.getenv("LOGIN_REDIRECT_URL", "/foobar")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == "True"
IN_PRODUCTION = not DEBUG

USE_X_FORWARDED_HOST = True
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


ALLOWED_HOSTS = [
    "127.0.0.1",
    "127.0.0.1:8000",
    "127.0.0.1:3000",
    "localhost",
    "localhost:8000",
    "localhost:3000",
    "dev.animalfoodbank.org",
]

INSTALLED_APPS = [
    "unfold",  # https://github.com/unfoldadmin/django-unfold
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "django_extensions",  # add this for 'python manage.py runserver_plus'
    "rest_framework",  # add DRF
    "rest_framework.authtoken",
    # "drf_registration",
    # 'djoser',
    "drfpasswordless",
    "django_filters",  # add DRF filters
    "phonenumber_field",
    "django_vite",  # May not need this? If using Vite/Vue for frontend via API.
    "afbcore",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    # 'afbcore.middleware.DebugCorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


VITE_APP_DIR = BASE_DIR.parent / "ui"

# https://github.com/adamchainz/django-cors-headers
CORS_ALLOW_ALL_ORIGINS = False
# CORS_ALLOW_HEADERS = []

# https://github.com/adamchainz/django-cors-headers#cors_allow_credentials
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # ViteJS dev server
    "http://127.0.0.1:3000",
    "http://localhost:8000",  # Django dev server
    "http://127.0.0.1:8000",
    "https://localhost",
    "https://dev.animalfoodbank.org",
    # TODO: Add production URL
]
CORS_ORIGIN_WHITELIST = CORS_ALLOWED_ORIGINS

# Resolves CSRF error:
#   Forbidden (Origin checking failed - http://127.0.0.1:3000 does not match any trusted origins.):
#
# See:
#   https://david.dev/django-origin-checking-failed-does-not-match-any-trusted-origins
#   https://github.com/adamchainz/django-cors-headers
#
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:3000",  # ViteJS dev server
    "http://127.0.0.1:3001",  # ViteJS dev server
    "http://localhost:3000",
    "https://localhost",
    "https://dev.animalfoodbank.org",
]

CSRF_USE_SESSIONS = False


CSRF_COOKIE_SECURE = IN_PRODUCTION
SESSION_COOKIE_SECURE = IN_PRODUCTION
SECURE_SSL_REDIRECT = False  # The reverse proxy handles this.

# This is needed for CSRF to work with CORS:
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-samesite
CSRF_COOKIE_SAMESITE = "None"

# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = False

# # May need to revisit this for production:
# https://docs.djangoproject.com/en/4.2/ref/csrf/#how-it-works
# CSRF_COOKIE_DOMAIN = ""

TOKEN_EXPIRED_AFTER_WEEKS = 2

# correspond to your build.outDir in your ViteJS configuration.
DJANGO_VITE_ASSETS_PATH = VITE_APP_DIR / "public"

# ViteJS webserver protocol (default : http).
DJANGO_VITE_DEV_SERVER_PROTOCOL = "http"

# ViteJS webserver hostname (default : localhost).
DJANGO_VITE_DEV_SERVER_HOST = "dev.animalfoodbank.org"

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
# This should be an initially empty destination directory. It's populated with
# the result of collectstatic during the deployment process. You should use
# the collectstatic management command to collect your static files in that
# directory. Then, your web server can serve the files in STATIC_ROOT.
#
# Add paths to STATICFILES_DIRS to include other directories and run:
#
#  $ python manage.py collectstatic
#
STATIC_ROOT = BASE_DIR / ".." / ".." / "public" / "static"

# For prod:
# https://docs.djangoproject.com/en/4.2/howto/static-files/deployment/#staticfiles-from-cdn
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-STORAGES
#
# This is ignored when using a CDN or reverse proxy for serving static files.
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
    DJANGO_VITE_ASSETS_PATH,
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        # "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
        # 'rest_framework.permissions.AllowAny',
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 25,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",  # for admin
        "rest_framework.authentication.TokenAuthentication",
    ],
}

# drfpasswordless
#
# For the default settings see:
# https://github.com/aaronn/django-rest-framework-passwordless
#
# Test commands:
# curl -X POST -d "email=delbo@solutious.com" localhost:8000/auth/email/
# curl -X POST -d "email=delbo@solutious.com&token=858997" localhost:8000/auth/token/
PASSWORDLESS_AUTH = {
    "PASSWORDLESS_AUTH_TYPES": ["EMAIL"],  # and/or 'MOBILE'
    "PASSWORDLESS_EMAIL_NOREPLY_ADDRESS": "noreply@animalfoodbank.org",  # or None
    "PASSWORDLESS_EMAIL_SUBJECT": "Your AFB login link",
    "PASSWORDLESS_EMAIL_TOKEN_HTML_TEMPLATE_NAME": "passwordless_token_email.html",
    # A plaintext verification email message overridden by the html message. Takes one string.
    "PASSWORDLESS_EMAIL_VERIFICATION_PLAINTEXT_MESSAGE": "Enter this verification code: %s",
    # The verification email template name.
    "PASSWORDLESS_EMAIL_VERIFICATION_TOKEN_HTML_TEMPLATE_NAME": "passwordless_verification_email.html",
    # Registers previously unseen aliases as new users.
    "PASSWORDLESS_REGISTER_NEW_USERS": True,
    # URL Prefix for Authentication Endpoints
    "PASSWORDLESS_AUTH_PREFIX": "auth/",
    # URL Prefix for Verification Endpoints
    "PASSWORDLESS_VERIFY_PREFIX": "auth/verify/",
    # Amount of time that tokens last, in seconds
    "PASSWORDLESS_TOKEN_EXPIRE_TIME": 15 * 60,  # 15 min
    # The user's email field name
    "PASSWORDLESS_USER_EMAIL_FIELD_NAME": "email",
    # Marks itself as verified the first time a user completes auth via token.
    # Automatically unmarks itself if email is changed. Use /auth/verify/email
    # for the address and /auth/verify for the token.
    "PASSWORDLESS_USER_MARK_EMAIL_VERIFIED": False,
    "PASSWORDLESS_USER_EMAIL_VERIFIED_FIELD_NAME": "email_verified",
    # Automatically send verification email or sms when a user changes their alias.
    "PASSWORDLESS_AUTO_SEND_VERIFICATION_TOKEN": False,
    # What function is called to construct an authentication tokens when
    # exchanging a passwordless token for a real user auth token. This function
    # should take a user and return a tuple of two values. The first value is
    # the token itself, the second is a boolean value representating whether
    # the token was newly created.
    "PASSWORDLESS_AUTH_TOKEN_CREATOR": "drfpasswordless.utils.create_authentication_token",
    # What function is called to construct a serializer for drf tokens when
    # exchanging a passwordless token for a real user auth token.
    "PASSWORDLESS_AUTH_TOKEN_SERIALIZER": "drfpasswordless.serializers.TokenResponseSerializer",
    # A dictionary of demo user's primary key mapped to their static pin
    "PASSWORDLESS_DEMO_USERS": {},
    # Configurable function for sending email
    "PASSWORDLESS_EMAIL_CALLBACK": "drfpasswordless.utils.send_email_with_callback_token",
    # Token Generation Retry Count
    "PASSWORDLESS_TOKEN_GENERATION_ATTEMPTS": 3,
}

# # For the default settings see:
# # https://drf-registration.readthedocs.io/en/latest/settings/index.html
# DRF_REGISTRATION = {
#     # General settings
#     "PROJECT_NAME": "AFB Requests",
#     "PROJECT_BASE_URL": "",
#     # User fields to register and respond to profile
#     "USER_FIELDS": (
#         "id",
#         "email",
#         # "password",
#         "name",
#         "is_active",
#     ),
#     "USER_READ_ONLY_FIELDS": (
#         "is_superuser",
#         "is_staff",
#         "is_active",
#     ),
#     "USER_SERIALIZER": "afbcore.serializers.UserSerializer",
#     "REGISTER_SERIALIZER": "afbcore.serializers.RegisterSerializer",
#     "USER_WRITE_ONLY_FIELDS": ("password",),
#     "REGISTER_SEND_WELCOME_EMAIL_ENABLED": True,
#     # For custom login username fields
#     "LOGIN_USERNAME_FIELDS": [
#         "email",
#     ],
#     "LOGOUT_REMOVE_TOKEN": True,
# }


PHONENUMBER_DB_FORMAT = "INTERNATIONAL"
PHONENUMBER_DEFAULT_FORMAT = "E164"
PHONENUMBER_DEFAULT_REGION = "CA"

ROOT_URLCONF = "afb.urls"

# Django-Tailwind
# https://django-tailwind.readthedocs.io/en/latest/installation.html#configuration

# TAILWIND_APP_NAME = "theme"

AUTH_USER_MODEL = "afbcore.User"

AUTHENTICATION_BACKENDS = [
    "drf_registration.auth.MultiFieldsModelBackend",
]

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


# Sending Email
# https://docs.djangoproject.com/en/5.0/ref/settings/#email-backend
# https://docs.djangoproject.com/en/5.0/topics/email/
#
# For development, you can use the console backend:
# 'django.core.mail.backends.console.EmailBackend'
#
#   OR
#
# Run an instance of Mailpit (https://github.com/axllent/mailpit) and use the
# SMTP backend:
# 'django.core.mail.backends.smtp.EmailBackend'
#

EMAIL_BACKEND = os.getenv("EMAIL_BACKEND")
EMAIL_TIMEOUT = os.getenv("EMAIL_TIMEOUT", 5)
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")


if DEBUG:
    INSTALLED_APPS += [
        "django.contrib.admindocs",
        "debug_toolbar",
    ]

    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE"),
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
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

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOG_LEVEL = "DEBUG" if DEBUG else "INFO"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": LOG_LEVEL,
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": LOG_LEVEL, "handlers": ["console"]},
}
