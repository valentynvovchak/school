import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEBUG = False

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'khodoriv-zosh1.herokuapp.com']
