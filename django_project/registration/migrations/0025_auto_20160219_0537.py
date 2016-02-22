# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0024_production_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='aboutus',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='production',
            name='address',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
    ]
