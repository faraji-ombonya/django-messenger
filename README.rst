============
django-messenger
============

django-messenger is a Django app that implements a Laravel like
notifications system.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "Django Messenger" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "django_messenger",
    ]

2. Run ``python manage.py migrate`` to create the models.
