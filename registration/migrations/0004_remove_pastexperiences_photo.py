# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_artist_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pastexperiences',
            name='photo',
        ),
    ]
