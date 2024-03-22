"""
WSGI config for testproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD:testproject/testproject/wsgi.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testproject.settings')

=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lasustechrepo.settings')
>>>>>>> laspotech_project/panywhere:lasustechrepo/lasustechrepo/wsgi.py
application = get_wsgi_application()
