# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0011_auto_20141126_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='hashed_id',
            field=models.SlugField(max_length=55, null=True),
            preserve_default=True,
        ),
    ]
