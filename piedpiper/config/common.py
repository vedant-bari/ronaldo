import os
from os.path import join
from distutils.util import strtobool
import dj_database_url
from configurations import Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Common(Configuration):

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sitemaps',
        'django.contrib.sites',
  
        # Third party apps
        'rest_framework',            # utilities for rest apis
        'rest_framework.authtoken',  # token authentication
        'django_filters',            # for filtering rest endpoints
        'anymail',
        'corsheaders',
        # Your apps
        'piedpiper.users',
        'taskapp',
        'piedpiper.todo',

        #'piedpiper.taskapp.apps.TaskappConfig',
        #'piedpiper.taskapp.apps.TaskappConfig
        #'django_celery_beat',
        #'django_celery_results',

        ##restauth
        'rest_auth',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'rest_auth.registration',


    )
    SITE_ID = 1
    # https://docs.djangoproject.com/en/2.0/topics/http/middleware/
    MIDDLEWARE = (
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
    )

    ALLOWED_HOSTS = ["*"]
    CORS_ORIGIN_ALLOW_ALL = True
    ROOT_URLCONF = 'piedpiper.urls'
    SECRET_KEY = 'DJANGO_SECRET_KEY'
    WSGI_APPLICATION = 'piedpiper.wsgi.application'

    ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILGUN_API_KEY": "key-5d7f36f3bd902a433e14a0f213124b7c",
    "MAILGUN_SENDER_DOMAIN": 'sandbox19484b242b4944d8889f040de15b27c2.mailgun.org',  # your Mailgun domain, if needed
    }
    EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"  # or sendgrid.EmailBackend, or...
    DEFAULT_FROM_EMAIL = "vedant.bari@analogyplus.com"  # if you don't already have this in settings
    SERVER_EMAIL = DEFAULT_FROM_EMAIL
    # Email
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    # EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
    # # Host for sending e-mail.
    # EMAIL_HOST = 'smtp.mailgun.org'
    #
    # # Port for sending e-mail.
    # EMAIL_PORT = 587
    #
    # # Optional SMTP authentication information for EMAIL_HOST.
    # EMAIL_HOST_USER = 'postmaster@sandbox19484b242b4944d8889f040de15b27c2.mailgun.org'
    # EMAIL_HOST_PASSWORD = 'f43401033e0c8096018adf48750a586c-dc5f81da-38cde9a8'
    # EMAIL_USE_TLS = False

    ADMINS = (
        ('Author', 'vedantbari40@gmail.com'),
    )

    # Postgres
    #DATABASES = {
    #    'default': dj_database_url.config(
    #        default='postgres://postgres:@postgres:5432/postgres',
    #        conn_max_age=int(os.getenv('POSTGRES_CONN_MAX_AGE', 600))
    #    )
    #}

    DATABASES = {
                'default': {
                            'ENGINE': 'django.db.backends.sqlite3',
                            'NAME': os.path.join(BASE_DIR , 'db.sqlite3'),
                            }
                }
    # General
    APPEND_SLASH = False
    TIME_ZONE = 'UTC'
    LANGUAGE_CODE = 'en-us'
    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = False
    USE_L10N = True
    USE_TZ = True
    LOGIN_REDIRECT_URL = '/'

    #JWT
    REST_USE_JWT = True
    REST_AUTH_SERIALIZERS = {
            'USER_DETAILS_SERIALIZER': 'piedpiper.users.serializers.UserDetailsSerializer',
            'JWT_SERIALIZER': 'piedpiper.users.serializers.JWTSerializer',
 
    'LOGIN_SERIALIZER': 'piedpiper.users.serializers.LoginSerializer',
    #'LOGIN_SERIALIZER' : 'rest_auth.serializers.LoginSerializer',   
    #'JWT_SERIALIZER': 'piedpiper.users.serializers.JWTSerializer',
    #'LOGIN_SERIALIZER': 'path.to.custom.LoginSerializer',
    #'TOKEN_SERIALIZER': 'path.to.custom.TokenSerializer',
    #...
    }
    REST_SESSION_LOGIN = False
    JWT_AUTH = {
        'JWT_VERIFY_EXPIRATION': False,
    } 
    REST_AUTH_REGISTER_SERIALIZERS = {
            'REGISTER_SERIALIZER': 'piedpiper.users.serializers.RegistrationSerializer'
    }
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    STATIC_ROOT = os.path.normpath(join(os.path.dirname(BASE_DIR), 'static'))
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'templates'),
    ]
    STATIC_URL = '/static/'
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    # Media files
    MEDIA_ROOT = join(os.path.dirname(BASE_DIR), 'media')
    MEDIA_URL = '/media/'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': STATICFILES_DIRS,
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
    # Celery settings
    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TIMEZONE = TIME_ZONE

    # Set DEBUG to False as a default for safety
    # https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = strtobool(os.getenv('DJANGO_DEBUG', 'no'))

    # Password Validation
    # https://docs.djangoproject.com/en/2.0/topics/auth/passwords/#module-django.contrib.auth.password_validation
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

    # Logging
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'django.server': {
                '()': 'django.utils.log.ServerFormatter',
                'format': '[%(server_time)s] %(message)s',
            },
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'handlers': {
            'django.server': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'django.server',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'propagate': True,
            },
            'django.server': {
                'handlers': ['django.server'],
                'level': 'INFO',
                'propagate': False,
            },
            'django.request': {
                'handlers': ['mail_admins', 'console'],
                'level': 'ERROR',
                'propagate': False,
            },
            'django.db.backends': {
                'handlers': ['console'],
                'level': 'INFO'
            },
        }
    }

    # Custom user app
    AUTH_USER_MODEL = 'users.User'

    # Django Rest Framework
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': int(os.getenv('DJANGO_PAGINATION_LIMIT', 10)),
        'DATETIME_FORMAT': '%Y-%m-%dT%H:%M:%S%z',
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.AllowAny',
            #'rest_framework.permissions.IsAuthenticated',
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
            #'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.TokenAuthentication',
        )
    }


    ACCOUNT_USERNAME_REQUIRED =False
