# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cineREST', '0002_film_on_screen'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='sinopsis',
            field=models.CharField(default=b'', max_length=400),
        ),
        migrations.AlterField(
            model_name='film',
            name='on_screen',
            field=models.BooleanField(default=False),
        ),
    ]
