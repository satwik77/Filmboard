# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_auto_20160123_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pastexperiences',
            name='user',
        ),
        migrations.RemoveField(
            model_name='recommendations',
            name='user',
        ),
    ]
