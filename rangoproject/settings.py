from pathlib import Path
import os



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#x1%!13km90&%)jz(9$*$vzo3(2k0r+n6=c=@0a@s2wxc#_9le'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Required for django-registration-redux

    'rangoapp',
    'registration',

    'login_history',
    'lockdown',
    
    "crispy_forms",
    "crispy_bootstrap5",
]

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'http://your-remote-server-ip:9200/', # Or your remote server if hosted on Elastic Cloud
    },
}

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

ASGI_APPLICATION = 'rangoproject.asgi.application'

# Set the site ID to 1 (or whatever your Site ID is)
SITE_ID = 1
REGISTRATION_OPEN = True
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'  # Redirect to login page after logout
#LOGIN_URL = '/login/'  # Ensure this points to the correct login page in your app


# Configure session settings (optional)
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Use the database to store session data
SESSION_COOKIE_AGE = 1209600  # 10 minutes (same as AUTO_LOGOUT IDLE_TIME)
#SESSION_COOKIE_AGE = 1209600  # Two weeks in seconds (default)
SESSION_COOKIE_SECURE = False  # Set to True for HTTPS-only
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Session expires when the browser is closed



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_auto_logout.middleware.auto_logout',
    #'lockdown.middleware.LockdownMiddleware', # To lock the entire site
]

LOCKDOWN_ENABLED= False
#LOCKDOWN_PASSWORDS = ('Admin', 'Root')


AUTO_LOGOUT = {
    'IDLE_TIME': 1209600,  # Log out after 10 minutes of inactivity (600 seconds)
    'SESSION_TIMEOUT': True,  # End session when user is auto-logged out
    'REDIRECT_TO_LOGIN_IMMEDIATELY': True,  # Redirect immediately to the login page upon logout
    'MESSAGE': 'You have been logged out due to inactivity. Please login again to continue.',
    }  # logout after 10 minutes of downtime


ROOT_URLCONF = 'rangoproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # !!! Add this !!!
                'django_auto_logout.context_processors.auto_logout_client',
            ],
        },
    },
]

WSGI_APPLICATION = 'rangoproject.wsgi.application'


# Bing Search API key
BING_API_KEY = 'your_bing_api_key'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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
        'OPTIONS': { 'min_length': 6, }
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "static"),
   ]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email configuration - using console backend for testing
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # For development/testing

