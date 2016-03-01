# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0031_projects_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastexperiences',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=b'pictures', blank=True),
        ),
    ]
