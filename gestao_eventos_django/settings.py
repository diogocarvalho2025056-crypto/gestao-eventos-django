import os
from pathlib import Path
import environ

# 1. Configuração do diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Inicialização do django-environ para ler o ficheiro .env
env = environ.Env()

# Bloqueia qualquer erro caso o ficheiro .env não seja encontrado pelo Python
try:
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
except Exception:
    pass

# Definições de Segurança com valores padrão (default) caso falhe o .env
SECRET_KEY = env('SECRET_KEY', default='chave-secreta-de-emergencia-123')
DEBUG = env.bool('DEBUG', default=True)
ALLOWED_HOSTS = ['*']

# 4. Aplicações instaladas (Inclui os módulos do Django e a tua app)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_eventos',  # A tua aplicação mapeada corretamente
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gestao_eventos_django.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'gestao_eventos_django.wsgi.application'

# 5. Configuração Dinâmica e Segura da Base de Dados MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME', default='eventos_db'),
        'USER': env('DB_USER', default='utilizador_eventos'),
        'PASSWORD': env('DB_PASSWORD', default='pass_eventos'),
        'HOST': env('DB_HOST', default='db'),  # 'db' é o nome do serviço no Docker
        'PORT': env('DB_PORT', default='3306'),
    }
}

# 6. Validação de Passwords
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.identity.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.identity.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.identity.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.identity.password_validation.NumericPasswordValidator',
    },
]

# 7. Internacionalização (Configurado para Portugal)
LANGUAGE_CODE = 'pt-pt'
TIME_ZONE = 'Europe/Lisbon'
USE_I18N = True
USE_TZ = True

# 8. Ficheiros Estáticos (CSS, JS, Imagens)
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] if os.path.exists(os.path.join(BASE_DIR, 'static')) else []
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'