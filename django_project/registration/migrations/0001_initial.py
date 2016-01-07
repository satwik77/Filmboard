# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('dob', models.DateField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('email_id', models.EmailField(max_length=254)),
                ('body_type', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=150)),
                ('skills', models.CharField(max_length=100)),
                ('education_background', models.TextField()),
                ('certifications', models.TextField()),
                ('phone', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Artists',
            },
        ),
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
            ],
            options={
                'verbose_name_plural': 'Recommendations',
            },
        ),
        migrations.AddField(
            model_name='artist',
            name='past_experiences',
            field=models.ManyToManyField(to='registration.PastExperiences', blank=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='recommendations',
            field=models.ManyToManyField(to='registration.Recommendations', blank=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
