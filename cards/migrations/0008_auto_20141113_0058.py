# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_auto_20141113_0055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='hashed_id',
            new_name='slug',
        ),
    ]
