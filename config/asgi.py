"""
ASGI config for RMO project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from config.settings.base import get_environment


os.environ.setdefault("DJANGO_SETTINGS_MODULE", get_environment())

application = get_asgi_application()
