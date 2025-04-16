from .base import * #noqa
from os import getenv, path
from dotenv import load_dotenv
from .base import BASE_DIR

local_env_path = path.join(BASE_DIR, '.envs', '.local.env')

if path.isfile(local_env_path):
    load_dotenv(local_env_path)



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("DEBUG")

SITE_NAME = getenv("SITE_NAME")

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = getenv("EMAIL_HOST")
EMAIL_PORT = getenv("EMAIL_PORT")
DEFAULT_FROM_EMAIL = getenv("DEFAULT_FROM_EMAIL")
DOMAIN = getenv("DOMAIN")
MAX_UPLOAD_SIZE = 1 * 1024 * 1024
