from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SQLITE = {
    'default': {
        'Engine': '',
        'NAME': os.path.join(BASE_DIR, 'db/sqlite/db.sqlite3')
    }
}

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'registros',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
