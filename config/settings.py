
"""
FitClub - Premium Fitness Management System

Django settings for config project.
Sport zali va fitness markazi boshqaruv tizimi.
"""

import os
from pathlib import Path




BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================================
# 2. XAVFSIZLIK SOZLAMALARI
# ==========================================

# Lokal ishlab chiqish uchun.
# Internetga joylashdan oldin maxfiy kalitni
# environment variable orqali sozlash kerak.

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-fitclub-local-development-key-change-me"
)

DEBUG = os.environ.get(
    "DJANGO_DEBUG",
    "True"
).lower() == "true"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


# ==========================================
# 3. O'RNATILGAN ILOVALAR
# ==========================================

INSTALLED_APPS = [

    # Django standart ilovalari
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # FitClub ilovalari
    "core",
    "accounts",
    "memberships",
'management',

]


# ==========================================
# 4. MIDDLEWARE
# ==========================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ==========================================
# 5. ASOSIY URL
# ==========================================

ROOT_URLCONF = "config.urls"


# ==========================================
# 6. HTML TEMPLATES
# ==========================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates",
        ],

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


# ==========================================
# 7. WSGI / ASGI
# ==========================================

WSGI_APPLICATION = "config.wsgi.application"

ASGI_APPLICATION = "config.asgi.application"


# ==========================================
# 8. MA'LUMOTLAR BAZASI
# ==========================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",

        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ==========================================
# 9. PAROL XAVFSIZLIGI
# ==========================================

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


# ==========================================
# 10. TIL VA VAQT
# ==========================================

LANGUAGE_CODE = "uz"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_TZ = True


# ==========================================
# 11. STATIC FAYLLAR
# CSS, JS, RASMLAR
# ==========================================

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"


# ==========================================
# 12. MEDIA FAYLLAR
# TRENER VA PROFIL RASMLARI
# ==========================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# ==========================================
# 13. DJANGO MODEL ID
# ==========================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ==========================================
# 14. LOGIN / LOGOUT
# ==========================================

LOGIN_URL = "login"

LOGIN_REDIRECT_URL = "dashboard"

LOGOUT_REDIRECT_URL = "home"




SESSION_COOKIE_AGE = 60 * 60 * 24 * 7

SESSION_SAVE_EVERY_REQUEST = False

SESSION_EXPIRE_AT_BROWSER_CLOSE = False

SESSION_COOKIE_HTTPONLY = True

SESSION_COOKIE_SAMESITE = "Lax"



CSRF_COOKIE_HTTPONLY = True

CSRF_COOKIE_SAMESITE = "Lax"



MAILERS = {
    "default": {
        "BACKEND": "django.core.mail.backends.console.EmailBackend",
    },
}



from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: "debug",
    messages.INFO: "info",
    messages.SUCCESS: "success",
    messages.WARNING: "warning",
    messages.ERROR: "error",
}


DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024

FILE_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024




SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = "DENY"
