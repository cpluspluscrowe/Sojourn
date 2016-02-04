"""
WSGI config for budget project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
import os
import sys
from django.core.wsgi import get_wsgi_application
sys.path.append('/home/ubuntu/Sojourn/budget/budget')
sys.path.append('/home/ubuntu/Sojourn/budget/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "budget.settings")

application = get_wsgi_application()
