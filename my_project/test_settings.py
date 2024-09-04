from my_project.settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.join(BASE_DIR, "db.sqlite3")
    }
}
