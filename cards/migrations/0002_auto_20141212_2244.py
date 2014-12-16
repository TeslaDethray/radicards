# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='extra_image',
            field=models.ImageField(default='', upload_to=b'/home/radicaldesigns/radicards/media/templates'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='art',
            name='image',
            field=models.ImageField(upload_to=b'/home/radicaldesigns/radicards/media/art'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(upload_to=b'/home/radicaldesigns/radicards/media/artist', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='font',
            name='font_file',
            field=models.FileField(null=True, upload_to=b'/home/radicaldesigns/radicards/media/fonts', blank=True),
            preserve_default=True,
        ),
    ]
