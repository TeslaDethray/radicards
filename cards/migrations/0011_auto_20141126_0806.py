# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0010_auto_20141125_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=55, blank=True),
            preserve_default=True,
        ),
    ]
