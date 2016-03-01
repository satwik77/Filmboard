# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0027_auto_20160222_2107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommendations',
            old_name='add_msg',
            new_name='remarks',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='recommendations',
        ),
        migrations.RemoveField(
            model_name='recommendations',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='recommendations',
            name='seek_from_name',
        ),
        migrations.RemoveField(
            model_name='recommendations',
            name='seek_from_type',
        ),
        migrations.AddField(
            model_name='recommendations',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
