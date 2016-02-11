# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0013_notifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='profile_pic',
            field=models.ImageField(upload_to=b'pictures', blank=True),
        ),
    ]
