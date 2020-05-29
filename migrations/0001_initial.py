# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayRaveModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='payrave_payravemodel', parent_link=True, to='cms.CMSPlugin', on_delete=models.CASCADE)),
                ('guest_name', models.CharField(max_length=50, default='Guest')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
