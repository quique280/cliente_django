"""
WSGI config for cliente_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/

Maria Alvarez Hernandez ID: 4-0239-0850
Luis Alonso Calderon Achio ID: 1-1702-0626
Enrique Diaz Delgado ID: 1-1725-0124
Derian Sibaja Chavarria ID 4-0232-0842
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cliente_django.settings')

application = get_wsgi_application()
