# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20160116_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectRequirements',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill', models.CharField(max_length=100)),
                ('numbers', models.IntegerField()),
                ('character', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Requirements',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_type', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=200)),
                ('project_status', models.CharField(max_length=100)),
                ('project_cost', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=150)),
                ('languages', models.CharField(max_length=400)),
                ('duration_start', models.DateField()),
                ('duration_end', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.AlterModelOptions(
            name='allied',
            options={'verbose_name_plural': 'Allied Services'},
        ),
        migrations.AlterModelOptions(
            name='production',
            options={'verbose_name_plural': 'Productions'},
        ),
        migrations.AddField(
            model_name='projects',
            name='producer',
            field=models.ManyToManyField(to='registration.production', blank=True),
        ),
        migrations.AddField(
            model_name='projectrequirements',
            name='project',
            field=models.ForeignKey(to='registration.Projects'),
        ),
    ]
