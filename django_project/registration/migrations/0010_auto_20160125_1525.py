# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0009_auto_20160123_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='producer',
            field=models.ManyToManyField(to='registration.Production', blank=True),
        ),
    ]
