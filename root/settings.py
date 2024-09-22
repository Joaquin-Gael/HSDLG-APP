from pathlib import Path
from schemas.user import UsuarioCliente
import os

ROOT = os.path.join(Path(__file__).parent)

BACKEND_ROOT = 'http://0.0.0.0:8000/'

API_URL = ''.join([BACKEND_ROOT, 'API/'])

MEDIA_URL = ''.join([BACKEND_ROOT,'media/'])

ASSETS_PATH = os.path.join(ROOT, 'assets')

DEBUG = True

AUTH_MODEL = UsuarioCliente