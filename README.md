# PAYRAVE

A rave( flutterwave payment api ) Plugin for Django CMS

## Getting Started

Payrave is a simple Django cms plugin for RAVE(flutterwave api) payment integration.

You will need to register with rave first
https://ravepay.co
and create a pay now button, please note the details of the button link.

### Prerequisites

NONE

### Installing

A step by step series of examples that tell you have to get a development env running

1.PIP INSTALL

```
 pip install payrave
```

2. Add "payrave" to your INSTALLED_APPS setting like this::

```
INSTALLED_APPS = [
        ...
        'payrave',
    ]
```

3. Migrate.

```
python manage.py migrate payrave 

```
ENJOY!!

## Built With

* [DjangoCMS](https://www.django-cms.org/) - The web framework used
* [RAVE](https://ravepay.co/) - Payment System


## Contributing

Please read [CONTRIBUTING.md](https://github.com/cleopatra27/payrave/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Cleopatra Douglas** - *Initial work* - [Django_Authentication1.7.9](https://github.com/cleopatra27/Django_Authentication1.7.9)


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/cleopatra27/payrave/blob/master/LICENSE.md) file for details


