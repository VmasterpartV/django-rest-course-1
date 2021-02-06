
BEFORE_DJANGO_APPS = (

)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PART_APPS = (
    'rest_framework',
    'django_filters',
)

LOCAL_APPS = (
    'aaaimx',
)

INSTALLED_APPS = BEFORE_DJANGO_APPS + DJANGO_APPS + THIRD_PART_APPS + LOCAL_APPS