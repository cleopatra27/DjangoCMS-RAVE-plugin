# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrave', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payravemodel',
            old_name='guest_name',
            new_name='data_PBFPubKey',
        ),
        migrations.AddField(
            model_name='payravemodel',
            name='data_amount',
            field=models.CharField(max_length=50, default='Guest'),
        ),
        migrations.AddField(
            model_name='payravemodel',
            name='data_countryguest_name',
            field=models.CharField(max_length=50, default='Guest'),
        ),
        migrations.AddField(
            model_name='payravemodel',
            name='data_currency',
            field=models.CharField(max_length=50, default='Guest'),
        ),
        migrations.AddField(
            model_name='payravemodel',
            name='data_custom_description',
            field=models.CharField(max_length=50, default='Guest'),
        ),
        migrations.AddField(
            model_name='payravemodel',
            name='data_custom_logo',
            field=models.CharField(max_length=50, default='Guest'),
        ),
        migrations.AddField(
            model_name='payravemodel',
            name='data_custom_title',
            field=models.CharField(max_length=50, default='Guest'),
        ),
        migrations.AddField(
            model_name='payravemodel',
            name='data_customer_email',
            field=models.CharField(max_length=50, default='Guest'),
        ),
        migrations.AddField(
            model_name='payravemodel',
            name='data_exclude_banks',
            field=models.CharField(max_length=50, default='Guest'),
        ),
        migrations.AddField(
            model_name='payravemodel',
            name='data_pay_button_text',
            field=models.CharField(max_length=50, default='Guest'),
        ),
        migrations.AddField(
            model_name='payravemodel',
            name='data_payment_methodguest_name',
            field=models.CharField(max_length=50, default='Guest'),
        ),
        migrations.AddField(
            model_name='payravemodel',
            name='data_redirect_url',
            field=models.CharField(max_length=50, default='Guest'),
        ),
        migrations.AddField(
            model_name='payravemodel',
            name='data_txref',
            field=models.CharField(max_length=50, default='Guest'),
        ),
    ]
