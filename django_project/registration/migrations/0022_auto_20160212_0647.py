# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0021_auto_20160211_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allied',
            name='category',
        ),
        migrations.RemoveField(
            model_name='allied',
            name='sub_category',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='skills',
        ),
        migrations.AddField(
            model_name='allied',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=b'pictures', blank=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='my_story',
            field=models.TextField(default=b' '),
        ),
        migrations.AddField(
            model_name='production',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=b'pictures', blank=True),
        ),
    ]
