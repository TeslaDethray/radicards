# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_template_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='hashed_id',
            field=models.SlugField(max_length=55),
            preserve_default=True,
        ),
    ]
