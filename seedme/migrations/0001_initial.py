# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-05 03:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea_status', models.IntegerField(choices=[(0, b'new'), (1, b'discussing'), (2, b'prototyping'), (3, b'alpha'), (4, b'beta'), (5, b'release')], default=0)),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('mtime', models.DateTimeField(auto_now=True)),
                ('need_help', models.BooleanField(default=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(choices=[(0, b'programmer'), (1, b'designer'), (2, b'ui/ux'), (3, b'marketer'), (4, b'sales'), (5, b'manager'), (6, b'other')])),
            ],
        ),
        migrations.CreateModel(
            name='ProgressLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('from_status', models.IntegerField(choices=[(0, b'new'), (1, b'discussing'), (2, b'prototyping'), (3, b'alpha'), (4, b'beta'), (5, b'release')])),
                ('to_status', models.IntegerField(choices=[(0, b'new'), (1, b'discussing'), (2, b'prototyping'), (3, b'alpha'), (4, b'beta'), (5, b'release')])),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seedme.Idea')),
            ],
        ),
        migrations.AddField(
            model_name='idea',
            name='need_profession_types',
            field=models.ManyToManyField(related_name='is_needed_by', to='seedme.ProfessionType'),
        ),
        migrations.AddField(
            model_name='idea',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='idea',
            name='participants',
            field=models.ManyToManyField(related_name='participate', to=settings.AUTH_USER_MODEL),
        ),
    ]
