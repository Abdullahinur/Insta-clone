"""
WSGI config for instaclone project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from whitenoise.django import DjangoWhiteNoise
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

project_folder = os.path.expanduser('instaclone')
load_dotenv(os.path.join(project_folder, '.env'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instaclone.settings.local")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
