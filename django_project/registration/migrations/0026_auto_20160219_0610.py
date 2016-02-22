# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0025_auto_20160219_0537'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='address',
            field=models.TextField(default=b' '),
        ),
        migrations.AlterField(
            model_name='production',
            name='aboutus',
            field=models.TextField(default=b' ', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='production',
            name='address',
            field=models.TextField(default=b' '),
        ),
    ]
