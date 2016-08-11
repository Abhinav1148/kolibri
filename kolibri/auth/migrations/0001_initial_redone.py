# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 17:25
from __future__ import unicode_literals

import django.core.validators
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters and digits only.', max_length=30, validators=[django.core.validators.RegexValidator('^\\w+$', 'Enter a valid username. This value may contain only letters and numbers.')], verbose_name='username')),
                ('full_name', models.CharField(blank=True, max_length=120, verbose_name='full name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='date joined')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(choices=[('facility', 'Facility'), ('classroom', 'Classroom'), ('learnergroup', 'LearnerGroup')], max_length=20)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('_default_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='FacilityDataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('allow_signups', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='FacilityUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters and digits only.', max_length=30, validators=[django.core.validators.RegexValidator('^\\w+$', 'Enter a valid username. This value may contain only letters and numbers.')], verbose_name='username')),
                ('full_name', models.CharField(blank=True, max_length=120, verbose_name='full name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='date joined')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityDataset')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.Collection')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityDataset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityUser')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('admin', 'Admin'), ('coach', 'Coach')], max_length=20)),
                ('collection', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.Collection')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityDataset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='kolibriauth.FacilityUser')),
            ],
        ),
        migrations.AddField(
            model_name='collection',
            name='dataset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.FacilityDataset'),
        ),
        migrations.AddField(
            model_name='collection',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='kolibriauth.Collection'),
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('kolibriauth.collection',),
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('kolibriauth.collection',),
        ),
        migrations.CreateModel(
            name='LearnerGroup',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('kolibriauth.collection',),
        ),
        migrations.AlterUniqueTogether(
            name='role',
            unique_together=set([('user', 'collection', 'kind')]),
        ),
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together=set([('user', 'collection')]),
        ),
        migrations.AddField(
            model_name='facilityuser',
            name='facility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kolibriauth.Facility'),
        ),
        migrations.AlterUniqueTogether(
            name='facilityuser',
            unique_together=set([('username', 'facility')]),
        ),
    ]
