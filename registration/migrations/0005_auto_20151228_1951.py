# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_remove_pastexperiences_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='email_id',
            field=models.EmailField(max_length=254),
        ),
    ]
