"""
Django settings for Tyraan_blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""


import os


ALLOWED_HOSTS = []
ADMIN_MEDIA_PREFIX = '/static/admin/' 
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

DUOSHUO_SECRET = 'tyraan_blog'
DUOSHUO_SHORTNAME = 'tyraan'
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    
        
    'tyraan',
    'duoshuo',    
                )
SECRET_KEY = '9bn$ftw%u83(k9n=%26s+-w=68&#*@ek)k@yob+^n(c2hln01o'

SITE_ID=2
STATIC_URL = '/static/'

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
      os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
     )

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)




# Application definition

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
)

ROOT_URLCONF = 'Tyraan_blog.urls'




# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Tyraan_blog',
        'USER': 'tyraan',
        'PASSWORD': 'tyraan',
        'HOST':'',
        'PORT':'',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'
TIME_ZONE = 'Asia/Beijing'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/




WSGI_APPLICATION = 'Tyraan_blog.wsgi.application'
