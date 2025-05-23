"""
Django settings for Core project.

Generated by 'django-admin startproject' using Django 5.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""
from dotenv import load_dotenv
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


load_dotenv()  # this loads the .env file into os.environ

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRETS")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# DEBUG = False

# ALLOWED_HOSTS = ['igniteandascend.com','www.igniteandascend.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'tinymce',
    'app',
    'books',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'Core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'app.context_processors.pagelinks'
            ],
        },
    },
]

WSGI_APPLICATION = 'Core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'  # or your local timezone

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

# Static files configration
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR/ 'staticfiles/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media files configuration
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin-allow-popups"

TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 50,
    'selector': 'textarea.tinymce',
    'theme': 'silver',
    'height': 600,
    'plugins': '''
        advlist autolink lists link image charmap print preview anchor
        searchreplace visualblocks code fullscreen
        insertdatetime media table paste code help wordcount
        hr pagebreak nonbreaking save directionality
        textcolor colorpicker textpattern imagetools
        codesample emoticons template
    ''',
    'toolbar1': '''
        undo redo | formatselect | bold italic underline strikethrough |
        forecolor backcolor | fontselect fontsizeselect |
        alignleft aligncenter alignright alignjustify |
        bullist numlist outdent indent | table |
        link image media | codesample emoticons template |
        hr pagebreak | removeformat | fullscreen preview save | code help
    ''',
    'contextmenu': 'link image inserttable | cell row column deletetable',
    'menubar': 'file edit view insert format tools table help',
    'statusbar': True,
    'branding': False,  # removes "Powered by TinyMCE"
    'image_caption': True,
    'quickbars_selection_toolbar': 'bold italic underline | quicklink h2 h3 blockquote quickimage quicktable',
    'quickbars_insert_toolbar': 'image media codesample template hr pagebreak',
    'nonbreaking_force_tab': True,
    'paste_data_images': True,  # allow pasting images directly
    'automatic_uploads': True,
    'file_picker_types': 'image media file',
    'content_style': 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }',

    # ALLOW BUTTONS AND MORE CUSTOM TAGS
    'extended_valid_elements': '''
        button[class|id|name|onclick|style|type],
        iframe[src|frameborder|style|scrolling|class|width|height|name|align],
        script[type|src],
        form[action|method|class|id|style],
        input[type|name|value|class|id|style|placeholder]
    ''',
    'valid_children': '+body[button|form|iframe|script]',
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("GMAIL_ID")
DEFAULT_FROM_EMAIL = os.getenv("GMAIL_ID")
EMAIL_HOST_PASSWORD = os.getenv("GMAIL_PASS")
EMAIL_USE_TLS = True

RAZOR_KEY_ID = os.getenv("RAZOR_KEY_ID")
RAZOR_KEY_SECRET = os.getenv("RAZOR_KEY_SECRET")
GOOGLE_APP_ID = os.getenv("GOOGLE_APP_ID")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CORS_ALLOW_ALL_ORIGINS = True

# settings.py
DATA_UPLOAD_MAX_MEMORY_SIZE = 104857600  # 100 MB in bytes
FILE_UPLOAD_MAX_MEMORY_SIZE = 104857600  # Optional, for in-memory uploads
