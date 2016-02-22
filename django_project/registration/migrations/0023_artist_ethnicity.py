# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0022_auto_20160212_0647'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='ethnicity',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
