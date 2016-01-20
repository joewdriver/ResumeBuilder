# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=25)),
                ('lname', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='EdHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
                ('degree_attained', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JobHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_description', models.CharField(max_length=500)),
                ('employer', models.CharField(max_length=100)),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
                ('end_salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='References',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ref_name', models.CharField(max_length=50)),
                ('ref_phone', models.CharField(max_length=15)),
                ('ref_email', models.CharField(max_length=100)),
                ('ref_employer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('statement', models.CharField(max_length=500)),
                ('low_salary', models.IntegerField(default=10000)),
                ('high_salary', models.IntegerField(default=10000000)),
                ('applicant', models.ForeignKey(to='resumes.Applicant')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill', models.CharField(max_length=25)),
                ('resume', models.ForeignKey(to='resumes.Resume')),
            ],
        ),
        migrations.AddField(
            model_name='references',
            name='resume',
            field=models.ForeignKey(to='resumes.Resume'),
        ),
        migrations.AddField(
            model_name='jobhistory',
            name='resume',
            field=models.ForeignKey(to='resumes.Resume'),
        ),
        migrations.AddField(
            model_name='edhistory',
            name='resume',
            field=models.ForeignKey(to='resumes.Resume'),
        ),
        migrations.AddField(
            model_name='edhistory',
            name='school',
            field=models.ForeignKey(to='resumes.School'),
        ),
    ]
