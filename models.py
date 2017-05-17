from django.db import models
from cms.models import CMSPlugin


class PayRaveModel(CMSPlugin):
    data_PBFPubKey = models.CharField(max_length=50, default='Guest')
    data_txref = models.CharField(max_length=50, default='Guest')
    data_amount = models.CharField(max_length=50, default='Guest')
    data_customer_email = models.CharField(max_length=50, default='Guest')
    data_currency = models.CharField(max_length=50, default='Guest')
    data_pay_button_text = models.CharField(max_length=50, default='Guest')
    data_countryguest_name = models.CharField(max_length=50, default='Guest')
    data_custom_title = models.CharField(max_length=50, default='Guest')
    data_custom_description = models.CharField(max_length=50, default='Guest')
    data_redirect_url = models.CharField(max_length=50, default='Guest')
    data_custom_logo = models.CharField(max_length=50, default='Guest')
    data_payment_methodguest_name = models.CharField(max_length=50, default='Guest')
    data_exclude_banks = models.CharField(max_length=50, default='Guest')


