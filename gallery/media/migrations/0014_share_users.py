# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 10:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('media', '0013_share_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='users',
            field=models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]