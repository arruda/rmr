
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin', 
    'django.contrib.admindocs',

    'django_extensions', 
    'model_utils', 
    'debug_toolbar',
    'taggit',
    'south',

#apps
    'books',
    'authors',
#libs
    'html5_boilerplate',
#    'utils',
    
#deploy
    'gunicorn',
)

