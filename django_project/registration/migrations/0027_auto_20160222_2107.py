# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0026_auto_20160219_0610'),
    ]

    operations = [
        migrations.AddField(
            model_name='allied',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='artist',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='production',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
    ]
