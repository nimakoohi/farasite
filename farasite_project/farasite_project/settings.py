from pathlib import Path
from dotenv import load_dotenv
import os

dotenv_path = '/home/niromusic/farasite_config/.env'

load_dotenv(dotenv_path)

X_FRAME_OPTIONS = 'DENY'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_COOKIE_AGE = 86400  # 86400 seconds = 1 day

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY'),

#On server side
DEBUG = True 
ALLOWED_HOSTS = ['farasite.com', '159.69.3.144', '127.0.0.1']

THUMBNAIL_DEBUG = True  # Helpful for debugging
THUMBNAIL_NAMESPACE = 'images'

THUMBNAIL_QUALITY = 90  # Adjust to desired quality
THUMBNAIL_UPSCALE = False  # Prevent upscaling if the original image is smaller

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'farasite',
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_email',  # <- if you want email capability.
    'two_factor',
    'two_factor.plugins.phonenumber',  # <- if you want phone number capability.
    'two_factor.plugins.email',  # <- if you want email capability.
    'django_jalali',
    'sorl.thumbnail',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django_otp.middleware.OTPMiddleware",  # Place it after AuthenticationMiddleware
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = 'farasite_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'farasite_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DJANGO_DB_NAME'),
        'USER': os.getenv('DJANGO_DB_USER'),
        'PASSWORD': os.getenv('DJANGO_DB_PASSWORD'),
        'HOST': os.getenv('DJANGO_DB_HOST'),
        'PORT': os.getenv('DJANGO_DB_PORT'),
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

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

# Internationalization
LANGUAGE_CODE = 'fa'
TIME_ZONE = "Asia/Tehran"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Specify the list of languages your site supports
LANGUAGES = [
    ('fa', 'Persian'),
    ('en', 'English'),
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'farasite' / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'farasite/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
