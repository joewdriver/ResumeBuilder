# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobhistory',
            name='job_title',
            field=models.CharField(default='TBA', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='title',
            field=models.CharField(default='TBA', max_length=50),
            preserve_default=False,
        ),
    ]
