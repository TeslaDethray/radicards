# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0009_card_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='image',
        ),
        migrations.RemoveField(
            model_name='font',
            name='external_url',
        ),
    ]
