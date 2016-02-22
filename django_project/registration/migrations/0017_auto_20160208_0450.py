# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0016_auto_20160202_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='aboutus',
            field=models.TextField(null=True, blank=True),
        ),
    ]
