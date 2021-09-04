import os
from pathlib import Path
import atexit

# SECURITY WARNING: don't run with EASY_SETUP_MODE turned on in production!
# Variable for fast project start without dealing with environment variables
EASY_RUN_MODE = False

if EASY_RUN_MODE:
    os.environ['SECRET_KEY'] = 'test'
    os.environ['DB_NAME'] = 'test_ascii_generator_db'
    os.environ['DB_USERNAME'] = 'test_ascii_generator_user'
    os.environ['DB_PASSWORD'] = 'test_ascii_generator_pass'
    os.environ['RECAPTCHA_PUBLIC_KEY'] = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'  # Those are test keys, don't bother
    os.environ['RECAPTCHA_PRIVATE_KEY'] = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
TEMPORARY_IMAGES = os.path.join(BASE_DIR, '_temporary_images/')
if not os.path.exists(TEMPORARY_IMAGES):
    print('WARNING! Temporary images folder is not found.')
    # raise NotADirectoryError("Temporary images folder is not found.")

# Import environment variables from python file if it exist. For local development only.
if os.path.exists(os.path.join(BASE_DIR, 'project\\env_vars.py')):
    from . import env_vars

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.getenv('DEBUG', False))
if EASY_RUN_MODE:
    DEBUG = True

ALLOWED_HOSTS = ['www.ascii-generator.site', '.ascii-generator.site',
                 'ascii-generator.site']

# If DEBUG is True - allow all hosts. For local development only.
if DEBUG:
    ALLOWED_HOSTS.append('*')

# Application definition

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CUSTOM_APPS = [
    'staff.apps.StaffConfig',
    'app.apps.AppConfig',
]

THIRD_PARTY_APPS = [
    'django_cleanup',
    'captcha',
    'rosetta',
]

INSTALLED_APPS = DEFAULT_APPS + CUSTOM_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'app.middleware.ForceDefaultLanguageMiddleware',  # Deletes "HTTP_ACCEPT_LANGUAGE" to keep default lang
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

db_sqlite3 = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}

db_postgresql = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': os.getenv('DB_NAME'),
    'USER': os.getenv('DB_USERNAME'),
    'PASSWORD': os.getenv('DB_PASSWORD'),
    'HOST': os.getenv('DB_HOST', 'localhost'),
    'PORT': os.getenv('DB_PORT', '5432')
}

# Database can be switched here between sqlite3 and postgresql
DATABASES = {
    'default': db_postgresql
}

# If EASY_RUN_MODE is True, use sqlite3
if EASY_RUN_MODE:
    DATABASES['default'] = db_sqlite3

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LOCALE_PATHS = (
    os.path.join(BASE_DIR, '_locale/'),
)

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en-us', 'English'),
    ('ru-RU', 'Русский')
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# RECAPTCHA API Keys

RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY')
if EASY_RUN_MODE:
    SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

# django-rosetta settings

ROSETTA_SHOW_AT_ADMIN_PANEL = True

# If DEBUG is True, at runserver exit delete all the temporary images
if DEBUG:
    def clear_temporary_images_folder():
        for file_name in os.listdir(TEMPORARY_IMAGES):
            if file_name != '.keep':  # Keep the .keep file
                os.remove(os.path.join(TEMPORARY_IMAGES, file_name))
    atexit.register(clear_temporary_images_folder)
