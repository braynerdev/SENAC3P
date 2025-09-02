
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7e^fnb#ezhr$3ivgb9ql=1rr-sfv8!ue(jiq$m=p=vvxx(sy@x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'onelingo'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #"whitenoise.middleware.WhiteNoiseMiddleware", #Apenas para produção
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'onelingo',
        'USER': 'brayner',
        'PASSWORD': '1208',
        'HOST': 'localhost',
        'PORT': '3306',
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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




# recursos de segurança
#SECURE_HSTS_SECONDS = 31536000 #definir o tempo, em segundos, que os navegadores devem lembrar que o site deve ser acessado apenas via HTTPS. EM SEGUNDOS
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True #será forçado a usar HTTPS.
#SECURE_CONTENT_TYPE_NOSNIFF = True #Evita que navegadores tentem adivinhar o tipo de conteúdo (MIME type) caso o servidor não o defina corretamente.
#SESSION_COOKIE_SECURE = True #Garante que os cookies de sessão só sejam enviados se a conexão for HTTPS.
#CSRF_COOKIE_SECURE = True #Exige que o cookie do CSRF só seja enviado em conexões HTTPS.
#CSRF_COOKIE_HTTPONLY = True #Evita que scripts JavaScript acessem o cookie do CSRF.
#X_FRAME_OPTIONS = 'SAMEORIGIN' #BLOQUEIA QUALQUER <IFRAME>, SE BOTAR 'SAMEORIGIN' ELE SO VAI PERMITIR IFRAME VINDO DO PROPRIO DOMINIO

#SECURE_SSL_REDIRECT = True #SO ATIVAR QUANDO SUBIR PARA PRODUÇÃO! #Essa configuração faz com que todas as requisições HTTP sejam automaticamente redirecionadas para HTTPS.