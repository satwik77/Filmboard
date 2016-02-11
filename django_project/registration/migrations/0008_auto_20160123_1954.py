# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0007_auto_20160123_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='PastExperiences',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_type', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=200)),
                ('project_status', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=300)),
                ('character_name', models.CharField(default=b'Not Applicable', max_length=200)),
                ('role_played', models.CharField(default=b'Not Applicable', max_length=200)),
                ('duration_start', models.DateField()),
                ('duration_end', models.DateField()),
                ('remarks', models.TextField()),
                ('special_mention', models.TextField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'experiences',
            },
        ),
        migrations.CreateModel(
            name='Recommendations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_type', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=200)),
                ('project_status', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=300)),
                ('character_name', models.CharField(default=b'Not Applicable', max_length=200)),
                ('role_played', models.CharField(default=b'Not Applicable', max_length=200)),
                ('duration_start', models.DateField()),
                ('duration_end', models.DateField()),
                ('seek_from_type', models.CharField(max_length=200)),
                ('seek_from_name', models.CharField(max_length=200)),
                ('email_id', models.EmailField(max_length=254)),
                ('add_msg', models.TextField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Recommendations',
            },
        ),
        migrations.AddField(
            model_name='artist',
            name='past_experiences',
            field=models.ManyToManyField(to='registration.PastExperiences', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='recommendations',
            field=models.ManyToManyField(to='registration.Recommendations', blank=True),
        ),
    ]
