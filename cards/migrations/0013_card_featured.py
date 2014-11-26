# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0012_card_hashed_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
