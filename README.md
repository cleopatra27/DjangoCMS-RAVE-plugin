# PAYRAVE

A rave( flutterwave payment api ) Plugin for Django CMS


# HOW TO INSTALL
=====
Payrave
=====

Payrave is a simple Django cms plugin for RAVE(flutterwave api) payment integration.

You will need to register with rave first
https://ravepay.co
and create a pay now button, please note the details of the button link.

Quick start
-----------

1. pip install payrave

2. Add "payrave" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'payrave',
    ]

3. Run python manage.py migrate payrave` to create the polls models.

And voila....
