"""
WSGI config for RMO project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from config.settings.base import get_environment

os.environ.setdefault("DJANGO_SETTINGS_MODULE", get_environment())

application = get_wsgi_application()
